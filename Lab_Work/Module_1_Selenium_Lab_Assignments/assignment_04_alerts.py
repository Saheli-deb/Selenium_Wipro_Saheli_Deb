"""Assignment 4: JavaScript Alerts, Confirm and Prompt.
Uses a local data URL so the exercise does not depend on a third-party site.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

html = """
<html><body>
<button id='alert' onclick='alert("Hello")'>Alert</button>
<button id='confirm' onclick='confirm("Continue?")'>Confirm</button>
<button id='prompt' onclick='prompt("Your name?")'>Prompt</button>
</body></html>
"""

driver = webdriver.Chrome()

try:
    driver.get("data:text/html;charset=utf-8," + html)

    driver.find_element(By.ID, "alert").click()
    alert = driver.switch_to.alert
    assert alert.text == "Hello"
    alert.accept()

    driver.find_element(By.ID, "confirm").click()
    confirm = driver.switch_to.alert
    confirm.dismiss()

    driver.find_element(By.ID, "prompt").click()
    prompt = driver.switch_to.alert
    prompt.send_keys("Saheli")
    prompt.accept()

    print("Assignment 4: PASS")

finally:
    driver.quit()
