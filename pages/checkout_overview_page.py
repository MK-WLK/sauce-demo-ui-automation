# Installed packages (Third-party)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_item_names(self):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )
        return [item.text for item in items]

    def get_payment_information(self):
        values = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.CLASS_NAME, "summary_value_label")
            )
        )
        return values[0].text

    def get_shipping_information(self):
        values = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.CLASS_NAME, "summary_value_label")
            )
        )
        return values[1].text

    def get_subtotal(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_subtotal_label")
            )
        ).text

    def get_tax(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_tax_label")
            )
        ).text

    def get_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        ).text

    def click_finish(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()

    def click_cancel(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "cancel"))
        ).click()