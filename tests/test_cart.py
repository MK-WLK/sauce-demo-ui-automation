# Installed packages (Third-party)
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_backpack_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page.add_backpack_to_cart()

    cart_count = inventory_page.get_cart_count()

    assert cart_count == "1"


def test_add_two_products_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    cart_count = inventory_page.get_cart_count()

    assert cart_count == "2"


def test_remove_backpack_from_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page.add_backpack_to_cart()
    inventory_page.remove_backpack_from_cart()

    cart_count = inventory_page.get_cart_count()

    assert cart_count == "0"