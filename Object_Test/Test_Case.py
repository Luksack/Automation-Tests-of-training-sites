import unittest
from selenium import webdriver
from Object_Test import Browser


class LoginSucces(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='/Users/lukaszsack/downloads/chromedriver')
        self.browser.implicitly_wait(15)

    def test_login(self):
        self.browser.get("http://www.phptravels.net/admin")

        login_page = Browser.LoginPage(self.browser)
        login_page.insert_email()
        login_page.insert_password()
        login_page.login_button_click()

        assert "Dashboard" in self.browser.title

        self.browser.save_screenshot('login_succes.png')

    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
