import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage
from utils.config_reader import ConfigReader


class TestProductSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.config = ConfigReader()

        browser = cls.config.get(
            "application",
            "browser"
        ).lower()

        if browser != "chrome":
            raise unittest.SkipTest(
                "Unittest implementation currently uses Chrome."
            )

        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        cls.driver = webdriver.Chrome(
            options=options
        )

        implicit_wait = cls.config.get_int(
            "application",
            "implicit_wait"
        )

        cls.driver.implicitly_wait(
            implicit_wait
        )

        base_url = cls.config.get(
            "application",
            "base_url"
        )

        cls.driver.get(base_url)

    def test_product_search_using_unittest(self):

        home_page = HomePage(
            self.driver
        )

        home_page.open_products()

        home_page.search_product(
            "dress"
        )

        self.assertTrue(
            home_page.search_results_displayed(),
            "SEARCHED PRODUCTS section was not displayed."
        )

        self.assertGreater(
            home_page.product_count(),
            0,
            "No products were found for the search."
        )

    @classmethod
    def tearDownClass(cls):

        if hasattr(cls, "driver"):

            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()