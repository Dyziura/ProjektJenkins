from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    """
    Login Page Object
    """

    USERNAME_FIELD = (By.ID, "username")

    def is_loaded(self):
        # Sprawdza, czy pole loginu jest widoczne
        return self.driver.find_element(*self.USERNAME_FIELD).is_displayed()