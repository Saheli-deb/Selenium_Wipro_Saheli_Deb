from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)

from pages.base_page import BasePage


class CartPage(BasePage):

    # ==========================================================
    # LOCATORS
    # ==========================================================

    CART_LINK = (
        By.XPATH,
        "//a[contains(@href,'/view_cart')]"
    )

    CART_TABLE = (
        By.ID,
        "cart_info_table"
    )

    CART_TABLE_FALLBACK = (
        By.XPATH,
        "//table[contains(@class,'cart_info')]"
    )

    CART_ROWS = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr"
    )

    PRODUCT_ROWS = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr[id^='product-']"
    )

    EMPTY_CART_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Cart is empty')]"
    )

    CONTINUE_SHOPPING_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Continue Shopping')]"
    )

    CHECKOUT_BUTTON = (
        By.XPATH,
        "//a[contains(@href,'/checkout')]"
    )

    # ==========================================================
    # PRODUCT ROW
    # ==========================================================

    def product_row(self, product_name):

        return (
            By.XPATH,
            "//tr[contains(@id,'product-')][.//td[contains(@class,'cart_description')]"
            "//a[normalize-space()=" + repr(product_name) + "]]"
        )

    # ==========================================================
    # OPEN CART
    # ==========================================================

    def open_cart(self):

        # First try the normal cart link
        try:

            cart_link = self.wait.until(
                EC.presence_of_element_located(
                    self.CART_LINK
                )
            )

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                cart_link
            )

            try:
                self.wait.until(
                    EC.element_to_be_clickable(
                        self.CART_LINK
                    )
                )

                cart_link.click()

            except (
                ElementClickInterceptedException,
                StaleElementReferenceException
            ):

                cart_link = self.wait.until(
                    EC.presence_of_element_located(
                        self.CART_LINK
                    )
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    cart_link
                )

        except TimeoutException:

            # Fallback: directly navigate to cart
            self.driver.get(
                "https://automationexercise.com/view_cart"
            )

        # Wait for URL
        try:

            self.wait.until(
                lambda driver:
                "/view_cart" in driver.current_url
            )

        except TimeoutException:

            # Final fallback
            self.driver.get(
                "https://automationexercise.com/view_cart"
            )

        # Wait for page to load
        self.wait.until(
            lambda driver:
            driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    # ==========================================================
    # CART DISPLAYED
    # ==========================================================

    def cart_displayed(self):

        # Primary locator
        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.CART_TABLE
                )
            )

            return True

        except TimeoutException:
            pass

        # Fallback locator
        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.CART_TABLE_FALLBACK
                )
            )

            return True

        except TimeoutException:
            return False

    # ==========================================================
    # PRODUCT DISPLAYED
    # ==========================================================

    def product_displayed(self, product_name):

        locator = self.product_row(product_name)

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    locator
                )
            )

            return True

        except TimeoutException:

            return False

    # ==========================================================
    # GET PRODUCT QUANTITY
    # ==========================================================

    def get_product_quantity(self, product_name):

        row = self.wait.until(
            EC.visibility_of_element_located(
                self.product_row(product_name)
            )
        )

        quantity = row.find_element(
            By.CSS_SELECTOR,
            "td.cart_quantity button"
        )

        return int(
            quantity.text.strip()
        )

    # ==========================================================
    # GET PRODUCT PRICE
    # ==========================================================

    def get_product_price(self, product_name):

        row = self.wait.until(
            EC.visibility_of_element_located(
                self.product_row(product_name)
            )
        )

        price = row.find_element(
            By.CSS_SELECTOR,
            "td.cart_price p"
        )

        return price.text.strip()

    # ==========================================================
    # GET PRODUCT TOTAL
    # ==========================================================

    def get_product_total(self, product_name):

        row = self.wait.until(
            EC.visibility_of_element_located(
                self.product_row(product_name)
            )
        )

        total = row.find_element(
            By.CSS_SELECTOR,
            "td.cart_total p"
        )

        return total.text.strip()

    # ==========================================================
    # NUMBER OF PRODUCTS IN CART
    # ==========================================================

    def get_product_count(self):

        try:

            products = self.wait.until(
                EC.presence_of_all_elements_located(
                    self.PRODUCT_ROWS
                )
            )

            return len(products)

        except TimeoutException:

            return 0

    # ==========================================================
    # INCREASE QUANTITY
    # ==========================================================

    def increase_quantity(self, product_name):

        """
        AutomationExercise does not provide a conventional
        + button in the cart.

        Quantity can be increased by adding the same product
        again from the Products page.
        """

        self.driver.get(
            "https://automationexercise.com/products"
        )

        self.wait.until(
            lambda driver:
            driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        # Search product
        search_box = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "search_product")
            )
        )

        search_box.clear()
        search_box.send_keys(product_name)

        search_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "submit_search")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            search_button
        )

        # Wait for searched product
        product_card = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'productinfo')][.//p[normalize-space()="
                    + repr(product_name)
                    + "]]"
                )
            )
        )

        add_button = product_card.find_element(
            By.XPATH,
            ".//a[contains(@class,'add-to-cart')]"
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            add_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_button
        )

        # Wait for add-cart modal
        try:

            continue_button = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(text(),'Continue Shopping')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                continue_button
            )

        except TimeoutException:
            pass

    # ==========================================================
    # REMOVE PRODUCT
    # ==========================================================

    def remove_product(self, product_name):

        row = self.wait.until(
            EC.presence_of_element_located(
                self.product_row(product_name)
            )
        )

        remove_button = row.find_element(
            By.CSS_SELECTOR,
            "td.cart_delete a"
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            remove_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            remove_button
        )

        # Wait until row disappears
        try:

            self.wait.until(
                EC.invisibility_of_element_located(
                    self.product_row(product_name)
                )
            )

        except TimeoutException:
            pass

    # ==========================================================
    # CHECKOUT
    # ==========================================================

    def checkout(self):

        button = self.wait.until(
            EC.presence_of_element_located(
                self.CHECKOUT_BUTTON
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # ==========================================================
    # CONTINUE SHOPPING
    # ==========================================================

    def continue_shopping(self):

        button = self.wait.until(
            EC.presence_of_element_located(
                self.CONTINUE_SHOPPING_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # ==========================================================
    # EMPTY CART
    # ==========================================================

    def cart_empty(self):

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.EMPTY_CART_MESSAGE
                )
            )

            return True

        except TimeoutException:

            return False