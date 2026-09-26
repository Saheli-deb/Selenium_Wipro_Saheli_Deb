import pytest
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from core.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
from utils.logger import get_logger


# =========================================================
# Global Configuration and Logger
# =========================================================

config = ConfigReader()
logger = get_logger()


# =========================================================
# Handle Advertisement / Promotional Overlays
# =========================================================

def handle_ad_overlay(driver):
    """
    Attempts to close known promotional overlays
    that may appear on Automation Exercise.

    If no overlay is present, execution continues normally.
    """

    possible_close_selectors = [
        "button[aria-label='Close']",
        "button[aria-label='close']",
        "[class*='close']",
        "[id*='close']",
        "[class*='Close']",
        "[id*='Close']",
    ]

    for selector in possible_close_selectors:

        try:

            elements = driver.find_elements(
                By.CSS_SELECTOR,
                selector
            )

            for element in elements:

                try:

                    if not element.is_displayed():
                        continue

                except Exception:
                    continue

                # -----------------------------------------
                # Normal click
                # -----------------------------------------

                try:

                    element.click()

                    logger.info(
                        "Promotional overlay closed."
                    )

                    return

                except Exception:
                    pass

                # -----------------------------------------
                # JavaScript fallback
                # -----------------------------------------

                try:

                    driver.execute_script(
                        "arguments[0].click();",
                        element
                    )

                    logger.info(
                        "Promotional overlay closed "
                        "using JavaScript."
                    )

                    return

                except Exception:
                    continue

        except Exception:
            continue


# =========================================================
# Hide Advertisement Iframes
# =========================================================

def hide_ad_iframes(driver):
    """
    Hides Google advertisement iframes that may intercept
    Selenium clicks.

    This function is intentionally lightweight.
    It does not wait for ads and does not fail the test
    if advertisements are unavailable.
    """

    try:

        driver.execute_script("""
            document.querySelectorAll(
                "iframe[title='Advertisement'], "
                "iframe[id^='aswift_']"
            ).forEach(function(frame) {

                frame.style.setProperty(
                    "display",
                    "none",
                    "important"
                );

                frame.style.setProperty(
                    "visibility",
                    "hidden",
                    "important"
                );

                frame.style.setProperty(
                    "pointer-events",
                    "none",
                    "important"
                );
            });
        """)

    except Exception:

        # Advertisement handling must never fail a test.
        pass


# =========================================================
# PyTest WebDriver Fixture
# =========================================================

@pytest.fixture
def driver(request):

    # -----------------------------------------------------
    # Read browser configuration
    # -----------------------------------------------------

    browser = config.get(
        "application",
        "browser"
    ).lower()

    headless = config.get_boolean(
        "application",
        "headless"
    )

    # -----------------------------------------------------
    # Create WebDriver through DriverFactory
    # -----------------------------------------------------

    driver = DriverFactory.create_driver(
        browser=browser,
        headless=headless
    )

    # -----------------------------------------------------
    # Configure implicit wait
    # -----------------------------------------------------

    implicit_wait = config.get_int(
        "application",
        "implicit_wait"
    )

    driver.implicitly_wait(
        implicit_wait
    )

    logger.info(
        f"Browser started: {browser}"
    )

    logger.info(
        f"Headless mode: {headless}"
    )

    logger.info(
        f"Implicit wait configured: {implicit_wait} seconds"
    )

    # -----------------------------------------------------
    # Launch application
    # -----------------------------------------------------

    base_url = config.get(
        "application",
        "base_url"
    )

    driver.get(base_url)

    logger.info(
        f"Application launched: {base_url}"
    )

    # -----------------------------------------------------
    # Give page a short opportunity to render
    # -----------------------------------------------------

    try:

        WebDriverWait(
            driver,
            2
        ).until(
            lambda d:
            d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    except Exception:

        pass

    # -----------------------------------------------------
    # Handle initial advertisements
    # -----------------------------------------------------

    handle_ad_overlay(driver)

    hide_ad_iframes(driver)

    # -----------------------------------------------------
    # Run test
    # -----------------------------------------------------

    yield driver

    # =====================================================
    # Failure Screenshot
    # =====================================================

    if hasattr(request.node, "rep_call"):

        if request.node.rep_call.failed:

            screenshot_dir = Path(
                config.get(
                    "report",
                    "screenshot_dir"
                )
            )

            screenshot_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            screenshot_path = (
                screenshot_dir /
                f"{request.node.name}.png"
            )

            try:

                driver.save_screenshot(
                    str(screenshot_path)
                )

                logger.error(
                    f"Test failed. Screenshot saved: "
                    f"{screenshot_path}"
                )

            except Exception as screenshot_error:

                logger.error(
                    f"Could not save failure screenshot: "
                    f"{screenshot_error}"
                )

    # =====================================================
    # Browser Cleanup
    # =====================================================

    try:

        driver.quit()

        logger.info(
            "Browser closed successfully"
        )

    except Exception:

        pass


# =========================================================
# PyTest Hook
# Makes test result available to fixture
# =========================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call
):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )