import unittest
from selenium import webdriver
from home_page import HomePage
from time import sleep

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com")
        self.home_page = HomePage(self.driver)
        self.driver.save_screenshot("screenshot.png")
        sleep(3)

    def tearDown(self):
        self.driver.quit()

class TestOpenPage(BaseTest):
    def test_open_home_page(self):
        # Przykładowa asercja: sprawdź tytuł strony
        self.assertIn("Selenium", self.driver.title)

if __name__ == "__main__":
    unittest.main()