import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.set_page_load_timeout(30)

    yield browser

    browser.quit()