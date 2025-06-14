from test_open_page import BaseTest
from home_page import HomePage
from login_page import LoginPage
from time import sleep

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

if __name__ == "__main__":
    import unittest
    unittest.main()