from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_LINK = (
        By.XPATH,
        "//a[contains(@href,'/login')]"
    )

    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        "[data-qa='login-email']"
    )

    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        "[data-qa='login-password']"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "[data-qa='login-button']"
    )

    LOGIN_HEADER = (
        By.XPATH,
        "//h2[normalize-space()='Login to your account']"
    )

    ERROR_MESSAGE = (
        By.XPATH,
        "//p[contains(text(),'Your email or password is incorrect')]"
    )

    LOGGED_IN_USER = (
        By.XPATH,
        "//a[contains(.,'Logged in as')]"
    )

    def open_login(self):

        self.click(self.LOGIN_LINK)

        self.wait.until(
            lambda driver: "/login" in driver.current_url
        )

    def login(self, email, password):

        self.enter_text(
            self.EMAIL_INPUT,
            email
        )

        self.enter_text(
            self.PASSWORD_INPUT,
            password
        )

        self.click(self.LOGIN_BUTTON)

    def login_page_displayed(self):

        return self.is_visible(
            self.LOGIN_HEADER
        )

    def invalid_login_message_displayed(self):

        return self.is_visible(
            self.ERROR_MESSAGE
        )

    def logged_in_displayed(self):

        return self.is_visible(
            self.LOGGED_IN_USER
        )