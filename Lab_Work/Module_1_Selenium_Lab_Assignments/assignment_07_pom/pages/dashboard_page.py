from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    INVENTORY = (By.ID, "inventory_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_displayed(self):
        self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY)
        )
        return True
