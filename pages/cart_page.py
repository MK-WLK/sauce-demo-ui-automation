
# Installed packages (Third-party)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            10,
            ignored_exceptions=(StaleElementReferenceException,)
    )

    def open(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()

    def remove_backpack(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "remove-sauce-labs-backpack")
            )
        ).click()

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        ).click()

    def click_continue_shopping(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue-shopping")
            )
        ).click()

