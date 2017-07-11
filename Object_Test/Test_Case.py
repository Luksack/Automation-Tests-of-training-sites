import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from Object_Test import Browser


class LoginSucces(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/lukaszsack/downloads/chromedriver')
        self.driver.implicitly_wait(15)

    def test_login_success(self):
        self.driver.get("http://www.phptravels.net/admin")

        login_page = Browser.LoginPage(self.driver)
        login_page.insert_email("admin@phptravels.com")
        login_page.insert_password("demoadmin")
        login_page.login_success_button_click()

        assert "Dashboard" in self.driver.title

        self.driver.save_screenshot('login_succes.png')

    def test_wrong_password(self):
        self.driver.get("http://www.phptravels.net/admin")

        login_page = Browser.LoginPage(self.driver)
        login_page.insert_email("admin@phptravels.com")
        login_page.insert_password("12345")
        login_page.login_fail_button_click()

        error_message = self.driver.find_element\
            (By.XPATH,
                    "//div [@class = 'alert alert-danger loading wow fadeIn animated animated']")
        self.assertEquals(error_message.text, "Invalid Login Credentials")

        self.driver.save_screenshot("Login_password_fail.png")

    def test_wrong_email(self):
        self.driver.get("http://www.phptravels.net/admin")

        login_page = Browser.LoginPage(self.driver)
        login_page.insert_email("wrong@email.com")
        login_page.insert_password("demoadmin")
        login_page.login_fail_button_click()

        error_message = self.driver.find_element\
            (By.XPATH,
                    "//div [@class = 'alert alert-danger loading wow fadeIn animated animated']")
        self.assertEquals(error_message.text, "Invalid Login Credentials")

    def test_empty_fields(self):
        self.driver.get("http://www.phptravels.net/admin")

        login_page = Browser.LoginPage(self.driver)
        login_page.insert_email("")
        login_page.insert_password("")
        login_page.login_empty_button_click()

        assert "dashboard" not in self.driver.title

        self.driver.save_screenshot("empty_validation.png")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
