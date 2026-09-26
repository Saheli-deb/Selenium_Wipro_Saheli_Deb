from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverFactory:
    """
    Centralized WebDriver creation.

    Supported browsers:
        - Chrome
        - Edge
        - Firefox
    """

    @staticmethod
    def create_driver(browser="chrome", headless=False):

        browser = browser.lower().strip()

        if browser == "chrome":

            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-infobars")

            driver = webdriver.Chrome(
                options=options
            )

        elif browser == "edge":

            options = EdgeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")

            driver = webdriver.Edge(
                options=options
            )

        elif browser == "firefox":

            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Firefox(
                options=options
            )

        else:

            raise ValueError(
                f"Unsupported browser: {browser}. "
                f"Supported browsers: chrome, edge, firefox."
            )

        return driver