from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "inventory" in driver.current_url

def test_login_with_invalid_password(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    ).send_keys("wrong_password")

    wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    ).text

    assert error_message == (
        "Epic sadface: Username and password do not match "
        "any user in this service"
    )

def test_login_with_empty_username(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    ).send_keys("secret_sauce")

    wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    ).text

    assert error_message == "Epic sadface: Username is required"

def test_login_with_empty_password(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    ).text

    assert error_message == "Epic sadface: Password is required"