from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException
)

from pages.base_page import BasePage


class SignupPage(BasePage):

    # =========================================================
    # SIGNUP / LOGIN
    # =========================================================

    LOGIN_LINK = (
        By.XPATH,
        "//a[contains(@href,'/login')]"
    )

    NAME_INPUT = (
        By.CSS_SELECTOR,
        "[data-qa='signup-name']"
    )

    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        "[data-qa='signup-email']"
    )

    SIGNUP_BUTTON = (
        By.CSS_SELECTOR,
        "[data-qa='signup-button']"
    )

    # =========================================================
    # ACCOUNT INFORMATION
    # =========================================================

    ACCOUNT_INFO_HEADER = (
        By.XPATH,
        "//b[normalize-space()='Enter Account Information']"
    )

    TITLE_MR = (
        By.ID,
        "id_gender1"
    )

    TITLE_MRS = (
        By.ID,
        "id_gender2"
    )

    PASSWORD_INPUT = (
        By.ID,
        "password"
    )

    DAY_SELECT = (
        By.ID,
        "days"
    )

    MONTH_SELECT = (
        By.ID,
        "months"
    )

    YEAR_SELECT = (
        By.ID,
        "years"
    )

    NEWSLETTER_CHECKBOX = (
        By.ID,
        "newsletter"
    )

    SPECIAL_OFFERS_CHECKBOX = (
        By.ID,
        "optin"
    )

    # =========================================================
    # ADDRESS
    # =========================================================

    FIRST_NAME = (
        By.ID,
        "first_name"
    )

    LAST_NAME = (
        By.ID,
        "last_name"
    )

    COMPANY = (
        By.ID,
        "company"
    )

    ADDRESS1 = (
        By.ID,
        "address1"
    )

    ADDRESS2 = (
        By.ID,
        "address2"
    )

    COUNTRY = (
        By.ID,
        "country"
    )

    STATE = (
        By.ID,
        "state"
    )

    CITY = (
        By.ID,
        "city"
    )

    ZIPCODE = (
        By.ID,
        "zipcode"
    )

    MOBILE_NUMBER = (
        By.ID,
        "mobile_number"
    )

    # =========================================================
    # CREATE ACCOUNT
    # =========================================================

    CREATE_ACCOUNT_BUTTON = (
        By.CSS_SELECTOR,
        "[data-qa='create-account']"
    )

    ACCOUNT_CREATED_HEADER = (
        By.XPATH,
        "//b[normalize-space()='Account Created!']"
    )

    CONTINUE_BUTTON = (
        By.CSS_SELECTOR,
        "[data-qa='continue-button']"
    )

    # =========================================================
    # LOGGED IN
    # =========================================================

    LOGGED_IN_USER = (
        By.XPATH,
        "//a[contains(normalize-space(.),'Logged in as')]"
    )

    # =========================================================
    # DELETE ACCOUNT
    # =========================================================

    DELETE_ACCOUNT = (
        By.XPATH,
        "//a[contains(@href,'/delete_account')]"
    )

    ACCOUNT_DELETED = (
        By.XPATH,
        "//b[normalize-space()='Account Deleted!']"
    )

    # =========================================================
    # ADVERTISEMENT HANDLING
    # =========================================================

    def hide_ads(self):

        try:

            self.driver.execute_script("""
                document.querySelectorAll(
                    "iframe[title='Advertisement'], "
                    "iframe[aria-label='Advertisement'], "
                    "iframe[id^='aswift_'], "
                    "iframe[id*='aswift']"
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

                document.querySelectorAll(
                    "ins.adsbygoogle, "
                    "[id*='google_ads'], "
                    "[class*='adsbygoogle']"
                ).forEach(function(ad) {

                    ad.style.setProperty(
                        "pointer-events",
                        "none",
                        "important"
                    );
                });
            """)

        except Exception:
            pass

    # =========================================================
    # OPEN SIGNUP PAGE
    # =========================================================

    def open_signup(self):

        self.hide_ads()

        login_link = self.wait.until(
            EC.presence_of_element_located(
                self.LOGIN_LINK
            )
        )

        try:

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                login_link
            )

        except Exception:
            pass

        try:

            self.wait.until(
                EC.element_to_be_clickable(
                    self.LOGIN_LINK
                )
            )

            login_link.click()

        except (
            ElementClickInterceptedException,
            TimeoutException
        ):

            self.hide_ads()

            login_link = self.wait.until(
                EC.presence_of_element_located(
                    self.LOGIN_LINK
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                login_link
            )

        self.wait.until(
            lambda driver:
            "/login" in driver.current_url.lower()
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.NAME_INPUT
            )
        )

    # =========================================================
    # INITIAL SIGNUP
    # =========================================================

    def signup(self, name, email):

        self.enter_text(
            self.NAME_INPUT,
            name
        )

        self.enter_text(
            self.EMAIL_INPUT,
            email
        )

        self.hide_ads()

        self.safe_click(
            self.SIGNUP_BUTTON
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.ACCOUNT_INFO_HEADER
            )
        )

    # =========================================================
    # SAFE CLICK
    # =========================================================

    def safe_click(self, locator):

        self.hide_ads()

        try:

            element = self.wait.until(
                EC.presence_of_element_located(
                    locator
                )
            )

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                element
            )

        except Exception:
            element = None

        # -----------------------------------------
        # Normal Selenium click
        # -----------------------------------------

        try:

            element = self.wait.until(
                EC.element_to_be_clickable(
                    locator
                )
            )

            element.click()

            return True

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException,
            TimeoutException
        ):

            pass

        # -----------------------------------------
        # Hide ads and retry
        # -----------------------------------------

        self.hide_ads()

        try:

            element = self.wait.until(
                EC.presence_of_element_located(
                    locator
                )
            )

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                element
            )

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

            return True

        except Exception:

            return False

    # =========================================================
    # SAFE CHECKBOX
    # =========================================================

    def safe_checkbox_click(self, locator):

        self.hide_ads()

        try:

            checkbox = self.wait.until(
                EC.presence_of_element_located(
                    locator
                )
            )

            # Already selected
            if checkbox.is_selected():
                return

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                checkbox
            )

        except Exception:
            checkbox = None

        # -----------------------------------------
        # Normal click
        # -----------------------------------------

        try:

            checkbox = self.wait.until(
                EC.element_to_be_clickable(
                    locator
                )
            )

            if not checkbox.is_selected():
                checkbox.click()

            return

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException,
            TimeoutException
        ):

            pass

        # -----------------------------------------
        # Hide advertisement and JS click
        # -----------------------------------------

        self.hide_ads()

        try:

            checkbox = self.wait.until(
                EC.presence_of_element_located(
                    locator
                )
            )

            if not checkbox.is_selected():

                self.driver.execute_script(
                    "arguments[0].click();",
                    checkbox
                )

            return

        except Exception:

            pass

        # -----------------------------------------
        # Final fallback
        # -----------------------------------------

        try:

            checkbox = self.wait.until(
                EC.presence_of_element_located(
                    locator
                )
            )

            self.driver.execute_script(
                """
                const checkbox = arguments[0];

                if (!checkbox.checked) {
                    checkbox.checked = true;

                    checkbox.dispatchEvent(
                        new Event('input', {
                            bubbles: true
                        })
                    );

                    checkbox.dispatchEvent(
                        new Event('change', {
                            bubbles: true
                        })
                    );
                }
                """,
                checkbox
            )

        except Exception:
            pass

    # =========================================================
    # SELECT BY VALUE
    # =========================================================

    def select_by_value(self, locator, value):

        element = self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

        self.driver.execute_script(
            """
            const select = arguments[0];
            const value = arguments[1];

            select.value = value;

            select.dispatchEvent(
                new Event('change', {
                    bubbles: true
                })
            );
            """,
            element,
            str(value)
        )

    # =========================================================
    # SELECT BY VISIBLE TEXT
    # =========================================================

    def select_by_visible_text(self, locator, text):

        element = self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

        self.driver.execute_script(
            """
            const select = arguments[0];
            const text = arguments[1];

            for (
                let i = 0;
                i < select.options.length;
                i++
            ) {

                if (
                    select.options[i].text.trim()
                    === text.trim()
                ) {

                    select.selectedIndex = i;

                    select.dispatchEvent(
                        new Event('change', {
                            bubbles: true
                        })
                    );

                    break;
                }
            }
            """,
            element,
            text
        )

    # =========================================================
    # FILL ACCOUNT INFORMATION
    # =========================================================

    def fill_account_information(
        self,
        title,
        password,
        day,
        month,
        year,
        first_name,
        last_name,
        company,
        address1,
        address2,
        country,
        state,
        city,
        zipcode,
        mobile_number
    ):

        # -----------------------------------------
        # Title
        # -----------------------------------------

        if str(title).strip().lower() in (
            "mr",
            "male"
        ):

            self.safe_click(
                self.TITLE_MR
            )

        else:

            self.safe_click(
                self.TITLE_MRS
            )

        # -----------------------------------------
        # Password
        # -----------------------------------------

        self.enter_text(
            self.PASSWORD_INPUT,
            password
        )

        # -----------------------------------------
        # Date of Birth
        # -----------------------------------------

        self.select_by_value(
            self.DAY_SELECT,
            day
        )

        self.select_by_value(
            self.MONTH_SELECT,
            month
        )

        self.select_by_value(
            self.YEAR_SELECT,
            year
        )

        # -----------------------------------------
        # Newsletter
        # -----------------------------------------

        self.safe_checkbox_click(
            self.NEWSLETTER_CHECKBOX
        )

        # -----------------------------------------
        # Special Offers
        # -----------------------------------------

        self.safe_checkbox_click(
            self.SPECIAL_OFFERS_CHECKBOX
        )

        # -----------------------------------------
        # First Name
        # -----------------------------------------

        self.enter_text(
            self.FIRST_NAME,
            first_name
        )

        # -----------------------------------------
        # Last Name
        # -----------------------------------------

        self.enter_text(
            self.LAST_NAME,
            last_name
        )

        # -----------------------------------------
        # Company
        # -----------------------------------------

        self.enter_text(
            self.COMPANY,
            company
        )

        # -----------------------------------------
        # Address 1
        # -----------------------------------------

        self.enter_text(
            self.ADDRESS1,
            address1
        )

        # -----------------------------------------
        # Address 2
        # -----------------------------------------

        self.enter_text(
            self.ADDRESS2,
            address2
        )

        # -----------------------------------------
        # Country
        # -----------------------------------------

        self.select_by_visible_text(
            self.COUNTRY,
            country
        )

        # -----------------------------------------
        # State
        # -----------------------------------------

        self.enter_text(
            self.STATE,
            state
        )

        # -----------------------------------------
        # City
        # -----------------------------------------

        self.enter_text(
            self.CITY,
            city
        )

        # -----------------------------------------
        # ZIP Code
        # -----------------------------------------

        self.enter_text(
            self.ZIPCODE,
            zipcode
        )

        # -----------------------------------------
        # Mobile Number
        # -----------------------------------------

        self.enter_text(
            self.MOBILE_NUMBER,
            mobile_number
        )

    # =========================================================
    # CREATE ACCOUNT
    # =========================================================

    def create_account(self):

        self.hide_ads()

        success = self.safe_click(
            self.CREATE_ACCOUNT_BUTTON
        )

        if not success:

            raise RuntimeError(
                "Create Account button could not be clicked."
            )

        # -----------------------------------------
        # Wait for Account Created page
        # -----------------------------------------

        self.wait.until(
            EC.visibility_of_element_located(
                self.ACCOUNT_CREATED_HEADER
            )
        )

        self.wait.until(
            lambda driver:
            "account_created" in
            driver.current_url.lower()
        )

    # =========================================================
    # ACCOUNT CREATED VERIFICATION
    # =========================================================

    def account_created_displayed(self):

        return self.is_visible(
            self.ACCOUNT_CREATED_HEADER
        )

    # =========================================================
    # CONTINUE AFTER ACCOUNT CREATION
    # =========================================================

    def continue_after_registration(self):

        self.hide_ads()

        button = self.wait.until(
            EC.presence_of_element_located(
                self.CONTINUE_BUTTON
            )
        )

        try:

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                button
            )

        except Exception:
            pass

        # -----------------------------------------
        # Normal click
        # -----------------------------------------

        try:

            self.wait.until(
                EC.element_to_be_clickable(
                    self.CONTINUE_BUTTON
                )
            )

            button.click()

        except Exception:

            # -------------------------------------
            # Advertisement fallback
            # -------------------------------------

            self.hide_ads()

            button = self.wait.until(
                EC.presence_of_element_located(
                    self.CONTINUE_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        # -----------------------------------------
        # Wait until homepage
        # -----------------------------------------

        self.wait.until(
            lambda driver:
            "account_created" not in
            driver.current_url.lower()
        )

        # -----------------------------------------
        # Wait until Logged in as appears
        # -----------------------------------------

        self.wait.until(
            EC.visibility_of_element_located(
                self.LOGGED_IN_USER
            )
        )

    # =========================================================
    # LOGGED IN VERIFICATION
    # =========================================================

    def logged_in_displayed(self):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(
                    self.LOGGED_IN_USER
                )
            )

            return element.is_displayed()

        except TimeoutException:

            return False

    # =========================================================
    # DELETE ACCOUNT
    # =========================================================

    def delete_account(self):

        self.hide_ads()

        delete_link = self.wait.until(
            EC.presence_of_element_located(
                self.DELETE_ACCOUNT
            )
        )

        try:

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                delete_link
            )

        except Exception:
            pass

        # -----------------------------------------
        # Normal click
        # -----------------------------------------

        try:

            self.wait.until(
                EC.element_to_be_clickable(
                    self.DELETE_ACCOUNT
                )
            )

            delete_link.click()

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException,
            TimeoutException
        ):

            # -------------------------------------
            # Advertisement fallback
            # -------------------------------------

            self.hide_ads()

            delete_link = self.wait.until(
                EC.presence_of_element_located(
                    self.DELETE_ACCOUNT
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                delete_link
            )

        # -----------------------------------------
        # Wait for Account Deleted
        # -----------------------------------------

        self.wait.until(
            EC.visibility_of_element_located(
                self.ACCOUNT_DELETED
            )
        )

    # =========================================================
    # ACCOUNT DELETED VERIFICATION
    # =========================================================

    def account_deleted_displayed(self):

        return self.is_visible(
            self.ACCOUNT_DELETED
        )