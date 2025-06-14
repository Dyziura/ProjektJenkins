from base_page import BasePage
from login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class HomePageLocators:
    """
    Home Page locators
    """
    myAccountButton = (By.CSS_SELECTOR, '#menu-item-22 > a > span') #Page Object naming convention

class HomePage(BasePage):
    """
    Home Page Object
    """
    def click_account_button(self):
        # 1. Znajdź przycisk Enter the store
        el = self.driver.find_element(*HomePageLocators.myAccountButton) # * to rozpakowanie krotki czyli *(By.ID, "login2") = By.ID, "login2"
        # 2. Kliknij w przycisk
        el.click()
        # Zwróć stronę katalogu
        return LoginPage(self.driver)