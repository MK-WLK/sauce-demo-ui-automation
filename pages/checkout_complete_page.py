
# Installed packages (Third-party)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_confirmation_header(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        ).text

    def get_confirmation_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-text")
            )
        ).text

    def click_back_home(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "back-to-products")
            )
        ).click()

    def click_generate_pdf_order(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[normalize-space()='Generate PDF order']"
                )
            )
        ).click()
    