import unittest
from selenium import webdriver
from Object_Test import Browser
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginSucces(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='/Users/lukaszsack/downloads/chromedriver')

    def test_login(self):
        browser = self.browser
        browser.get("http://www.phptravels.net/admin")

        login_page = Browser.Page_Login(self.browser)
        login_page.insert_email()
        login_page.insert_password()
        login_page.login_button_click()

        time.sleep(4)
    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()
