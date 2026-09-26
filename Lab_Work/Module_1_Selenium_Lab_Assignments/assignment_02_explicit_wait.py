"""Assignment 2: Synchronization & Explicit Waits
No time.sleep() is used. WebDriverWait + expected_conditions is used.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Selenium's own dynamic page is useful for wait practice.
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    ).click()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    assert message.text == "Hello World!"
    print("Loaded text:", message.text)
    print("Assignment 2: PASS")

finally:
    driver.quit()
