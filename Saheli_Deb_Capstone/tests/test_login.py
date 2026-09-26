import pytest

from pages.login_page import LoginPage
from utils.csv_reader import CSVReader


LOGIN_DATA = CSVReader.read(
    "test_data/login_data.csv"
)


@pytest.mark.regression
@pytest.mark.parametrize(
    "data",
    LOGIN_DATA
)
def test_invalid_login(driver, data):

    login_page = LoginPage(driver)

    login_page.open_login()

    assert login_page.login_page_displayed(), (
        "Login page was not displayed."
    )

    login_page.login(
        data["email"],
        data["password"]
    )

    assert login_page.invalid_login_message_displayed(), (
        "Invalid login error message was not displayed."
    )