"""Assignment 6: Windows, Tabs and Iframes.
Switches into an iframe, opens a new tab, reads title, closes it and returns.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Iframe
    driver.get("https://the-internet.herokuapp.com/iframe")

    frame = wait.until(
        EC.presence_of_element_located((By.ID, "mce_0_ifr"))
    )
    driver.switch_to.frame(frame)

    body = wait.until(
        EC.presence_of_element_located((By.ID, "tinymce"))
    )
    body.clear()
    body.send_keys("Module 1 iframe test")
    assert "Module 1 iframe test" in body.text

    driver.switch_to.default_content()

    # New tab
    driver.execute_script("window.open('https://www.selenium.dev/', '_blank');")

    original = driver.current_window_handle
    handles = driver.window_handles
    new_handle = [h for h in handles if h != original][0]

    driver.switch_to.window(new_handle)
    assert "Selenium" in driver.title
    print("New tab title:", driver.title)

    driver.close()
    driver.switch_to.window(original)

    print("Assignment 6: PASS")

finally:
    driver.quit()
