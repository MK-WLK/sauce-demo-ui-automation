from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()

    def add_bike_light_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bike-light"
        ).click()

    def remove_backpack_from_cart(self):
        self.driver.find_element(
            By.ID, "remove-sauce-labs-backpack"
        ).click()

    def get_cart_count(self):
        badges = self.driver.find_elements(
            By.CLASS_NAME, "shopping_cart_badge"
        )

        if not badges:
            return "0"

        return badges[0].text