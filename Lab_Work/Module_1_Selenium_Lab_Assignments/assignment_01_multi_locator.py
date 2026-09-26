"""Assignment 1: The Multi-Locator Challenge
Uses ID, NAME and XPATH locators and validates the resulting URL.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.saucedemo.com/")

    # By.ID
    username = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    # By.NAME is demonstrated on the password field.
    # SauceDemo uses id="password"; name may vary by version.
    # Use NAME where available, otherwise fall back to ID.
    try:
        password = driver.find_element(By.NAME, "password")
    except Exception:
        password = driver.find_element(By.ID, "password")

    password.send_keys("secret_sauce")

    # By.XPATH
    login_button = driver.find_element(
        By.XPATH, "//input[@type='submit' or @value='Login']"
    )
    login_button.click()

    wait.until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url
    print("Assignment 1: PASS")

finally:
    driver.quit()
