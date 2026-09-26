import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def load_test_data():
    with open("login_test_data.csv", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


@pytest.mark.parametrize("case", load_test_data())
def test_login_with_external_data(case):
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://www.saucedemo.com/")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(case["username"])

        driver.find_element(By.NAME, "password").send_keys(case["password"])
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        if case["expected"] == "success":
            WebDriverWait(driver, 10).until(
                lambda d: "/inventory.html" in d.current_url
            )
            assert "/inventory.html" in driver.current_url
        else:
            error = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
            )
            assert "Epic sadface" in error.text

    finally:
        driver.quit()
