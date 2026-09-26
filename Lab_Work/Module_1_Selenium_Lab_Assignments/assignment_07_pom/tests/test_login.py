from selenium import webdriver
from assignment_07_pom.pages.login_page import LoginPage
from assignment_07_pom.pages.dashboard_page import DashboardPage


def test_login():
    driver = webdriver.Chrome()

    try:
        login = LoginPage(driver)
        dashboard = DashboardPage(driver)

        login.open()
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        assert "/inventory.html" in driver.current_url
        assert dashboard.is_displayed()

    finally:
        driver.quit()
