from test_open_page import BaseTest
from home_page import HomePage
from login_page import LoginPage
from time import sleep
import os
from selenium.webdriver.common.by import By


class HomeTest(BaseTest):
    def setUp(self):
        super().setUp()
        # Przejście do strony logowania przez kliknięcie przycisku "Moje konto"
        sleep(3)
        self.login_page = self.home_page.click_account_button()
        sleep(3)

    def test_login_page_loaded(self):
        # Sprawdź, czy strona logowania się załadowała
        self.assertTrue(self.login_page.is_loaded(), "Strona logowania nie została załadowana")

    def test_insert_email(self):
        email = os.environ.get("EMAIL")
        self.driver.find_element(By.ID, "reg_email").send_keys(email)
        sleep(2)
        print(f"Wprowadzono email: {email}")

    def test_insert_password(self):
        password = os.environ.get("TEST_PASSWORD")
        self.driver.find_element(By.ID, "reg_password").send_keys(password)
        sleep(2)
        print(f"Wprowadzono haslo: {password}")

if __name__ == "__main__":
    import unittest
    unittest.main()