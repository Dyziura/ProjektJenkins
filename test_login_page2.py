import pytest
from home_page import HomePage

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com")
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    home_page = HomePage(driver)
    return home_page.click_account_button()

def test_login_page_loaded(login_page):
    assert login_page.is_loaded(), "Strona logowania nie została załadowana"