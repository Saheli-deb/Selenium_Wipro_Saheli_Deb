import time

from pages.signup_page import SignupPage


def test_user_signup(driver):

    # =====================================================
    # Create a unique email for every test run
    # =====================================================

    unique_email = (
        f"saheli_{int(time.time())}@example.com"
    )

    signup_page = SignupPage(driver)

    # =====================================================
    # 1. Open Signup / Login page
    # =====================================================

    signup_page.open_signup()

    # =====================================================
    # 2. Start registration
    # =====================================================

    signup_page.signup(
        name="Saheli Test User",
        email=unique_email
    )

    # =====================================================
    # 3. Verify Account Information page
    # =====================================================

    assert signup_page.is_visible(
        signup_page.ACCOUNT_INFO_HEADER
    ), "Account Information page was not displayed"

    # =====================================================
    # 4. Fill Account Information
    # =====================================================

    signup_page.fill_account_information(
        title="Mrs",
        password="Test@12345",
        day="10",
        month="5",
        year="2000",
        first_name="Saheli",
        last_name="Test",
        company="Wipro",
        address1="Kolkata",
        address2="New Town",
        country="India",
        state="West Bengal",
        city="Kolkata",
        zipcode="700156",
        mobile_number="9876543210"
    )

    # =====================================================
    # 5. Create Account
    # =====================================================

    signup_page.create_account()

    # =====================================================
    # 6. Verify Account Created
    # =====================================================

    assert signup_page.account_created_displayed(), \
        "Account was not created successfully"

    # =====================================================
    # 7. Continue to Homepage
    # =====================================================

    signup_page.continue_after_registration()

    # =====================================================
    # 8. Verify User is Logged In
    # =====================================================

    assert signup_page.logged_in_displayed(), \
        "User was not logged in after registration"

    # =====================================================
    # 9. Delete Account
    # =====================================================

    signup_page.delete_account()

    # =====================================================
    # 10. Verify Account Deleted
    # =====================================================

    assert signup_page.account_deleted_displayed(), \
        "Account was not deleted successfully"