from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
    StaleElementReferenceException
)

from pages.base_page import BasePage


class HomePage(BasePage):

    # =====================================================
    # Navigation
    # =====================================================

    PRODUCTS_LINK = (
        By.XPATH,
        "//a[contains(normalize-space(), 'Products')]"
    )

    CART_LINK = (
        By.XPATH,
        "//a[contains(normalize-space(), 'Cart')]"
    )

    # =====================================================
    # Product Search
    # =====================================================

    SEARCH_INPUT = (
        By.NAME,
        "search"
    )

    SEARCH_BUTTON = (
        By.ID,
        "submit_search"
    )

    SEARCH_RESULTS_HEADER = (
        By.XPATH,
        "//h2[contains("
        "translate(normalize-space(.),"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
        "'abcdefghijklmnopqrstuvwxyz'),"
        "'searched products'"
        ")]"
    )

    PRODUCT_RESULTS = (
        By.CSS_SELECTOR,
        ".features_items .product-image-wrapper"
    )

    # =====================================================
    # Add To Cart
    # =====================================================

    PRODUCT_CARD = (
        By.XPATH,
        "//div[contains(@class,'product-image-wrapper')]"
    )

    ADD_TO_CART_BUTTON = (
        By.XPATH,
        ".//a[contains(@class,'add-to-cart')]"
    )

    # =====================================================
    # Add To Cart Modal
    # =====================================================

    CONTINUE_SHOPPING_BUTTON = (
        By.XPATH,
        "//button[contains(normalize-space(),'Continue Shopping')]"
    )

    PRODUCT_ADDED_MESSAGE = (
        By.XPATH,
        "//div[contains(@class,'modal-content')]"
        "//h4[contains(normalize-space(),'Added!')]"
    )

    # =====================================================
    # Advertisement Handling
    # =====================================================

    def hide_ad_iframes(self):
        """
        Hide Google advertisement iframes.

        AutomationExercise sometimes places an advertisement
        over Selenium elements. This can cause:
        ElementClickInterceptedException
        """

        try:

            self.driver.execute_script("""
                document.querySelectorAll(
                    "iframe[title='Advertisement'], "
                    "iframe[id^='aswift_'], "
                    "iframe[src*='doubleclick.net']"
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
            """)

        except Exception:
            pass

    # =====================================================
    # Scroll To Element
    # =====================================================

    def scroll_to_element(self, element):

        try:

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
            pass

    # =====================================================
    # Open Products Page
    # =====================================================

    def open_products(self):

        products_url = (
            "https://automationexercise.com/products"
        )

        self.driver.get(products_url)

        try:

            self.wait.until(
                EC.presence_of_element_located(
                    self.SEARCH_INPUT
                )
            )

        except TimeoutException:

            self.driver.get(products_url)

            self.wait.until(
                EC.presence_of_element_located(
                    self.SEARCH_INPUT
                )
            )

        self.hide_ad_iframes()

        self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

    # =====================================================
    # Search Product
    # =====================================================

    def search_product(self, product_name):

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

        search_box.clear()

        search_box.send_keys(
            product_name
        )

        self.hide_ad_iframes()

        search_button = self.wait.until(
            EC.presence_of_element_located(
                self.SEARCH_BUTTON
            )
        )

        self.scroll_to_element(
            search_button
        )

        try:

            self.wait.until(
                EC.element_to_be_clickable(
                    self.SEARCH_BUTTON
                )
            )

            search_button.click()

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):

            self.hide_ad_iframes()

            search_button = self.wait.until(
                EC.presence_of_element_located(
                    self.SEARCH_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                search_button
            )

        self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_RESULTS_HEADER
            )
        )

        self.hide_ad_iframes()

    # =====================================================
    # Verify Search Results
    # =====================================================

    def search_results_displayed(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.SEARCH_RESULTS_HEADER
                )
            ).is_displayed()

        except TimeoutException:

            return False

    # =====================================================
    # Count Products
    # =====================================================

    def product_count(self):

        products = self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_RESULTS
            )
        )

        return len(products)

    # =====================================================
    # Find Product Card
    # =====================================================

    def get_product_card(self, product_name):
        """
        Finds the product card using the product name.
        """

        locator = (
            By.XPATH,
            "//div[contains(@class,'product-image-wrapper')]"
            "[.//p[normalize-space()="
            f"'{product_name}'"
            "]]"
        )

        return self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

    # =====================================================
    # Add Product To Cart
    # =====================================================

    def add_product_to_cart(self, product_name):
        """
        Add a specific product to cart.

        Example:
            home_page.add_product_to_cart("Blue Top")
        """

        # -------------------------------------------------
        # Make sure ads are hidden
        # -------------------------------------------------

        self.hide_ad_iframes()

        # -------------------------------------------------
        # Find product card
        # -------------------------------------------------

        product_card = self.get_product_card(
            product_name
        )

        # -------------------------------------------------
        # Scroll product into center
        # -------------------------------------------------

        self.scroll_to_element(
            product_card
        )

        # -------------------------------------------------
        # Find Add To Cart button INSIDE that product
        # -------------------------------------------------

        add_button = product_card.find_element(
            *self.ADD_TO_CART_BUTTON
        )

        # -------------------------------------------------
        # Scroll button into view
        # -------------------------------------------------

        self.scroll_to_element(
            add_button
        )

        # -------------------------------------------------
        # Hide advertisements again
        # -------------------------------------------------

        self.hide_ad_iframes()

        # -------------------------------------------------
        # Normal click
        # -------------------------------------------------

        try:

            self.wait.until(
                lambda driver:
                add_button.is_displayed()
                and add_button.is_enabled()
            )

            add_button.click()

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):

            # -------------------------------------------------
            # Re-fetch product/button in case DOM changed
            # -------------------------------------------------

            self.hide_ad_iframes()

            product_card = self.get_product_card(
                product_name
            )

            add_button = product_card.find_element(
                *self.ADD_TO_CART_BUTTON
            )

            self.scroll_to_element(
                add_button
            )

            # -------------------------------------------------
            # JS click fallback
            # -------------------------------------------------

            self.driver.execute_script(
                "arguments[0].click();",
                add_button
            )

        # -------------------------------------------------
        # Wait for Add To Cart modal
        # -------------------------------------------------

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.CONTINUE_SHOPPING_BUTTON
                )
            )

        except TimeoutException:

            # Sometimes the modal loads slightly later.
            # Check once more after hiding advertisements.

            self.hide_ad_iframes()

            self.wait.until(
                EC.presence_of_element_located(
                    self.CONTINUE_SHOPPING_BUTTON
                )
            )

        # -------------------------------------------------
        # Close "Added!" modal
        # -------------------------------------------------

        self.close_add_to_cart_popup()

    # =====================================================
    # Close Add To Cart Popup
    # =====================================================

    def close_add_to_cart_popup(self):

        self.hide_ad_iframes()

        try:

            continue_button = self.wait.until(
                EC.presence_of_element_located(
                    self.CONTINUE_SHOPPING_BUTTON
                )
            )

            self.scroll_to_element(
                continue_button
            )

            try:

                continue_button.click()

            except ElementClickInterceptedException:

                self.hide_ad_iframes()

                continue_button = self.wait.until(
                    EC.presence_of_element_located(
                        self.CONTINUE_SHOPPING_BUTTON
                    )
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    continue_button
                )

        except TimeoutException:

            # Popup is already closed / did not appear.
            pass

    # =====================================================
    # Add Multiple Products
    # =====================================================

    def add_multiple_products_to_cart(
        self,
        product_names
    ):
        """
        Add multiple products.

        Example:
            home_page.add_multiple_products_to_cart([
                "Blue Top",
                "Men Tshirt"
            ])
        """

        for product_name in product_names:

            self.add_product_to_cart(
                product_name
            )

    # =====================================================
    # Open Cart
    # =====================================================

    def open_cart(self):

        self.hide_ad_iframes()

        cart = self.wait.until(
            EC.presence_of_element_located(
                self.CART_LINK
            )
        )

        self.scroll_to_element(
            cart
        )

        try:

            cart.click()

        except ElementClickInterceptedException:

            self.hide_ad_iframes()

            cart = self.wait.until(
                EC.presence_of_element_located(
                    self.CART_LINK
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                cart
            )

    # =====================================================
    # Product Exists
    # =====================================================

    def product_displayed(self, product_name):

        locator = (
            By.XPATH,
            "//div[contains(@class,'product-image-wrapper')]"
            f"[.//p[normalize-space()='{product_name}']]"
        )

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    locator
                )
            ).is_displayed()

        except TimeoutException:

            return False