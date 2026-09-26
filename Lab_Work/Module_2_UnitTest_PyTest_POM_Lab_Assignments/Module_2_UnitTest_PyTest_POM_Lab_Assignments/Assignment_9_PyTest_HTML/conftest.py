import os
import pytest


@pytest.fixture
def driver():
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is not None:
            os.makedirs("screenshots", exist_ok=True)
            safe_name = item.nodeid.replace("/", "_").replace("\\", "_")
            path = os.path.join("screenshots", safe_name + ".png")
            driver.save_screenshot(path)
