import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def load_data():
    with open("login_test_data.json", encoding="utf-8") as file:
        return json.load(file)


@pytest.mark.parametrize("case", load_data())
def test_login_from_json(case):
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys(case["username"])
        driver.find_element(By.NAME, "password").send_keys(case["password"])
        driver.find_element(By.ID, "login-button").click()

        if case["expected"] == "success":
            assert "/inventory.html" in driver.current_url
        else:
            assert "Epic sadface" in driver.find_element(
                By.CSS_SELECTOR, "h3[data-test='error']"
            ).text
    finally:
        driver.quit()
