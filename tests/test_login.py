# Installed packages (Third-party)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Local files
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "inventory" in driver.current_url

def test_login_with_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert error_message == (
        "Epic sadface: Username and password do not match "
        "any user in this service"
    )

def test_login_with_empty_username(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert error_message == "Epic sadface: Username is required"

def test_login_with_empty_password(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert error_message == "Epic sadface: Password is required"
