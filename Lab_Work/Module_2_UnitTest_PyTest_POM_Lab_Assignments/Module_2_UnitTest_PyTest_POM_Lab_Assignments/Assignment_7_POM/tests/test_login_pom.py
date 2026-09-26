import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_valid_login(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url
    assert dashboard.is_loaded()
