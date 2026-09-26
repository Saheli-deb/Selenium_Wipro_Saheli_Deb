from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException
)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =====================================================
    # Hide Google Advertisement Iframes
    # =====================================================

    def hide_ads(self):

        try:
            self.driver.execute_script("""
                const selectors = [
                    "iframe[title='Advertisement']",
                    "iframe[aria-label='Advertisement']",
                    "iframe[id^='aswift_']",
                    "iframe[src*='doubleclick.net']",
                    "iframe[src*='googlesyndication.com']"
                ];

                selectors.forEach(function(selector) {
                    document.querySelectorAll(selector).forEach(function(frame) {

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

                        frame.style.setProperty(
                            "z-index",
                            "-9999",
                            "important"
                        );
                    });
                });
            """)

        except Exception:
            pass

    # =====================================================
    # Safe Click
    # =====================================================

    def click(self, locator):

        # First remove advertisements
        self.hide_ads()

        for attempt in range(3):

            try:

                element = self.wait.until(
                    EC.presence_of_element_located(locator)
                )

                # Scroll element to center
                self.driver.execute_script(
                    """
                    arguments[0].scrollIntoView({
                        behavior: 'instant',
                        block: 'center',
                        inline: 'center'
                    });
                    """,
                    element
                )

                # Hide ads again after scrolling
                self.hide_ads()

                try:

                    self.wait.until(
                        EC.element_to_be_clickable(locator)
                    )

                    element.click()

                    return

                except ElementClickInterceptedException:

                    # Hide overlay and retry
                    self.hide_ads()

                    element = self.wait.until(
                        EC.presence_of_element_located(locator)
                    )

                    self.driver.execute_script(
                        "arguments[0].click();",
                        element
                    )

                    return

            except StaleElementReferenceException:

                if attempt == 2:
                    raise

            except TimeoutException:

                if attempt == 2:
                    raise

                self.hide_ads()

        # Last-resort JavaScript click
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # =====================================================
    # Safe Checkbox / Radio Click
    # =====================================================

    def click_checkbox(self, locator):

        self.hide_ads()

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        # Scroll checkbox into view
        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'instant',
                block: 'center',
                inline: 'center'
            });
            """,
            element
        )

        # Hide ads after scrolling
        self.hide_ads()

        try:

            # Normal click
            if not element.is_selected():

                try:
                    element.click()

                except ElementClickInterceptedException:

                    self.hide_ads()

                    self.driver.execute_script(
                        "arguments[0].click();",
                        element
                    )

        except StaleElementReferenceException:

            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            if not element.is_selected():

                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )

        # Verify checkbox state
        self.wait.until(
            lambda driver:
            driver.find_element(
                *locator
            ).is_selected()
        )

    # =====================================================
    # Enter Text
    # =====================================================

    def enter_text(self, locator, text):

        self.hide_ads()

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'instant',
                block: 'center',
                inline: 'center'
            });
            """,
            element
        )

        element.clear()
        element.send_keys(text)

    # =====================================================
    # Get Text
    # =====================================================

    def get_text(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    # =====================================================
    # Visibility
    # =====================================================

    def is_visible(self, locator):

        try:

            self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return True

        except TimeoutException:

            return False

    # =====================================================
    # Presence
    # =====================================================

    def is_present(self, locator):

        try:

            self.wait.until(
                EC.presence_of_element_located(locator)
            )

            return True

        except TimeoutException:

            return False

    # =====================================================
    # Page Title
    # =====================================================

    def get_title(self):

        return self.driver.title

    # =====================================================
    # Current URL
    # =====================================================

    def get_current_url(self):

        return self.driver.current_url