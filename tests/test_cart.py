# Installed packages (Third-party)
from selenium.webdriver.support.ui import WebDriverWait

# Local files
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_add_backpack_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"


def test_add_two_products_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    assert inventory_page.get_cart_count() == "2"


def test_remove_backpack_from_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.remove_backpack()

    assert inventory_page.get_cart_count() == "0"


def test_checkout_button_opens_checkout_information(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.click_checkout()

    assert logged_in_driver.current_url.endswith(
        "/checkout-step-one.html"
    )


def test_checkout_requires_first_name(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.click_checkout()

    checkout_page.click_continue()

    assert checkout_page.get_error_message() == (
        "Error: First Name is required"
    )


def test_checkout_requires_last_name(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Mark")
    checkout_page.click_continue()

    assert checkout_page.get_error_message() == (
        "Error: Last Name is required"
    )


def test_checkout_requires_postal_code(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Mark")
    checkout_page.enter_last_name("Walker")
    checkout_page.click_continue()

    assert checkout_page.get_error_message() == (
        "Error: Postal Code is required"
    )


def test_valid_checkout_opens_overview(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Mark")
    checkout_page.enter_last_name("Walker")
    checkout_page.enter_postal_code("12345")
    checkout_page.click_continue()

    assert logged_in_driver.current_url.endswith(
        "/checkout-step-two.html"
    )


def test_checkout_overview_displays_order_details(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)
    overview_page = CheckoutOverviewPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Mark")
    checkout_page.enter_last_name("Walker")
    checkout_page.enter_postal_code("12345")
    checkout_page.click_continue()

    assert overview_page.get_item_names() == ["Sauce Labs Backpack"]
    assert overview_page.get_payment_information() == "SauceCard #31337"
    assert overview_page.get_shipping_information() == (
        "Free Pony Express Delivery!"
    )
    assert overview_page.get_subtotal() == "Item total: $29.99"
    assert overview_page.get_tax() == "Tax: $2.40"
    assert overview_page.get_total() == "Total: $32.39"


def test_successful_checkout_displays_confirmation(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)
    overview_page = CheckoutOverviewPage(logged_in_driver)
    complete_page = CheckoutCompletePage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Mark")
    checkout_page.enter_last_name("Walker")
    checkout_page.enter_postal_code("12345")
    checkout_page.click_continue()

    overview_page.click_finish()

    assert complete_page.get_confirmation_header() == (
        "Thank you for your order!"
    )
    assert complete_page.get_confirmation_message() == (
        "Your order has been dispatched, and will arrive just as fast "
        "as the pony can get there!"
    )


def test_back_home_returns_to_inventory(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)
    overview_page = CheckoutOverviewPage(logged_in_driver)
    complete_page = CheckoutCompletePage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Mark")
    checkout_page.enter_last_name("Walker")
    checkout_page.enter_postal_code("12345")
    checkout_page.click_continue()

    overview_page.click_finish()
    complete_page.click_back_home()

    assert logged_in_driver.current_url.endswith("/inventory.html")


def test_generate_pdf_order_downloads_pdf(logged_in_driver, tmp_path):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)
    overview_page = CheckoutOverviewPage(logged_in_driver)
    complete_page = CheckoutCompletePage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    cart_page.open()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Mark")
    checkout_page.enter_last_name("Walker")
    checkout_page.enter_postal_code("12345")
    checkout_page.click_continue()

    overview_page.click_finish()
    complete_page.click_generate_pdf_order()

    pdf_file = WebDriverWait(logged_in_driver, 15).until(
        lambda _: next(
            (
                file
                for file in tmp_path.iterdir()
                if file.suffix.lower() == ".pdf"
            ),
            False,
        )
    )

    assert pdf_file.stat().st_size > 0
