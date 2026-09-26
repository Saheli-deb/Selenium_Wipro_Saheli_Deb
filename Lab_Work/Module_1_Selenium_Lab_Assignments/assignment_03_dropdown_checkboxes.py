"""Assignment 3: Dynamic Dropdowns & Checkboxes
Demonstrates checkbox state validation and an autocomplete-style selection.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Checkbox practice page
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    boxes = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "input[type='checkbox']")
        )
    )

    # Select both checkboxes.
    for box in boxes:
        if not box.is_selected():
            box.click()

    assert all(box.is_selected() for box in boxes)
    print("Checkboxes selected:", len(boxes))

    # Autocomplete practice page.
    driver.get("https://jqueryui.com/autocomplete/")
    driver.switch_to.frame(
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    )

    search = wait.until(
        EC.element_to_be_clickable((By.ID, "tags"))
    )
    search.send_keys("Ja")

    suggestions = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "ul.ui-autocomplete li")
        )
    )

    target = "Java"
    for option in suggestions:
        if option.text.strip() == target:
            option.click()
            break

    assert search.get_attribute("value") == target
    print("Autocomplete selected:", target)
    print("Assignment 3: PASS")

finally:
    driver.quit()
