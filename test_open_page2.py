import pytest
from selenium import webdriver
from home_page import HomePage
from time import sleep

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com")
    home_page = HomePage(driver)
    driver.save_screenshot("screenshot.png")
    sleep(3)
    yield driver, home_page
    driver.quit()

def test_open_home_page(setup):
    driver, home_page = setup
    assert "Selenium" in driver.title