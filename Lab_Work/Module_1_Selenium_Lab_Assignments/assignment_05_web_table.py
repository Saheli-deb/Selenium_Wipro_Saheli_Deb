"""Assignment 5: HTML Web Table Extractor.
Iterates rows/columns, locates a row by name and retrieves the Status value.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://the-internet.herokuapp.com/tables")

    table = wait.until(
        EC.presence_of_element_located((By.ID, "table1"))
    )

    headers = [
        h.text.strip()
        for h in table.find_elements(By.CSS_SELECTOR, "thead th")
    ]

    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

    target_name = "Smith"
    target_status = None

    for row in rows:
        cells = [c.text.strip() for c in row.find_elements(By.TAG_NAME, "td")]
        if target_name in cells:
            target_status = cells[headers.index("Due") - 1] if "Due" in headers else cells[-1]
            print("Matching row:", cells)
            break

    assert target_status is not None
    print("Retrieved value:", target_status)
    print("Assignment 5: PASS")

finally:
    driver.quit()
