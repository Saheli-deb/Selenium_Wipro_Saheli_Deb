import pytest

from pages.home_page import HomePage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver):

    home_page = HomePage(driver)
    cart_page = CartPage(driver)

    # ==========================================================
    # STEP 1 - Open Products
    # ==========================================================

    home_page.open_products()

    # ==========================================================
    # STEP 2 - Search Product
    # ==========================================================

    home_page.search_product("Blue Top")

    # ==========================================================
    # STEP 3 - Add Product
    # ==========================================================

    home_page.add_product_to_cart("Blue Top")

    # ==========================================================
    # STEP 4 - Open Cart
    # ==========================================================

    cart_page.open_cart()

    # ==========================================================
    # STEP 5 - Verify Cart Page
    # ==========================================================

    assert "/view_cart" in driver.current_url, \
        "User was not redirected to the cart page"

    assert cart_page.cart_displayed(), \
        "Cart table was not displayed"

    # ==========================================================
    # STEP 6 - Verify Product
    # ==========================================================

    assert cart_page.product_displayed("Blue Top"), \
        "Blue Top was not added to the cart"

    # ==========================================================
    # STEP 7 - Verify Quantity
    # ==========================================================

    quantity = cart_page.get_product_quantity(
        "Blue Top"
    )

    assert quantity == 1, \
        f"Expected quantity 1 but got {quantity}"

    # ==========================================================
    # STEP 8 - Verify Price
    # ==========================================================

    price = cart_page.get_product_price(
        "Blue Top"
    )

    assert price == "Rs. 500", \
        f"Unexpected product price: {price}"


def test_increase_product_quantity(driver):

    home_page = HomePage(driver)
    cart_page = CartPage(driver)

    # ==========================================================
    # Open Products
    # ==========================================================

    home_page.open_products()

    # ==========================================================
    # Search Product
    # ==========================================================

    home_page.search_product("Blue Top")

    # ==========================================================
    # Add Product First Time
    # ==========================================================

    home_page.add_product_to_cart("Blue Top")

    # ==========================================================
    # Open Cart
    # ==========================================================

    cart_page.open_cart()

    assert cart_page.cart_displayed(), \
        "Cart table was not displayed"

    assert cart_page.product_displayed("Blue Top"), \
        "Blue Top was not found in cart"

    # ==========================================================
    # Verify Initial Quantity
    # ==========================================================

    quantity_before = cart_page.get_product_quantity(
        "Blue Top"
    )

    assert quantity_before == 1, \
        f"Initial quantity should be 1, got {quantity_before}"

    # ==========================================================
    # Increase Quantity
    # ==========================================================

    cart_page.increase_quantity(
        "Blue Top"
    )

    # ==========================================================
    # Return To Cart
    # ==========================================================

    cart_page.open_cart()

    assert cart_page.cart_displayed(), \
        "Cart table was not displayed after increasing quantity"

    # ==========================================================
    # Verify Quantity = 2
    # ==========================================================

    quantity_after = cart_page.get_product_quantity(
        "Blue Top"
    )

    assert quantity_after == 2, \
        f"Expected quantity 2 but got {quantity_after}"


def test_remove_product_from_cart(driver):

    home_page = HomePage(driver)
    cart_page = CartPage(driver)

    # ==========================================================
    # Open Products
    # ==========================================================

    home_page.open_products()

    # ==========================================================
    # Search Product
    # ==========================================================

    home_page.search_product("Blue Top")

    # ==========================================================
    # Add Product
    # ==========================================================

    home_page.add_product_to_cart("Blue Top")

    # ==========================================================
    # Open Cart
    # ==========================================================

    cart_page.open_cart()

    assert cart_page.cart_displayed(), \
        "Cart table was not displayed"

    # ==========================================================
    # Verify Product
    # ==========================================================

    assert cart_page.product_displayed("Blue Top"), \
        "Blue Top was not added"

    # ==========================================================
    # Remove Product
    # ==========================================================

    cart_page.remove_product(
        "Blue Top"
    )

    # ==========================================================
    # Verify Product Removed
    # ==========================================================

    assert not cart_page.product_displayed(
        "Blue Top"
    ), \
        "Blue Top was not removed from cart"