
# Installed packages (Third-party)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "last-name"))
        ).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "postal-code"))
        ).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()

    def click_cancel(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "cancel"))
        ).click()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        ).text
