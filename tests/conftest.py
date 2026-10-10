# Installed packages (Third-party)
import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver(tmp_path):
    options = webdriver.ChromeOptions()

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "download.default_directory": str(tmp_path),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "plugins.always_open_pdf_externally": True,
        },
    )

    # Use headless Chrome when running in CI
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(30)

    yield browser

    browser.quit()


@pytest.fixture
def logged_in_driver(driver):
    from pages.login_page import LoginPage

    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    return driver
