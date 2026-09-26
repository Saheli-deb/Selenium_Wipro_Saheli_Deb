import pytest

from pages.home_page import HomePage
from utils.csv_reader import CSVReader


PRODUCT_DATA = CSVReader.read_csv(
    "test_data/product_search.csv"
)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "product_data",
    PRODUCT_DATA
)
def test_product_search(driver, product_data):

    home_page = HomePage(driver)

    home_page.open_products()

    product_name = product_data["product"]

    home_page.search_product(product_name)

    assert home_page.search_results_displayed(), (
        f"SEARCHED PRODUCTS section was not "
        f"displayed for '{product_name}'."
    )

    product_count = home_page.product_count()

    assert product_count > 0, (
        f"No products found for '{product_name}'."
    )