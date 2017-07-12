import unittest

from selenium import webdriver

from Object_Test import LoginPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/lukaszsack/downloads/chromedriver')
        self.driver.implicitly_wait(15)
        LoginPage.LoginPage.open_site(self)

    def test_login_success(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.set_email("admin@phptravels.com")
        login_page.set_password("demoadmin")
        login_page.login_success_button_click()

        assert "Dashboard" in self.driver.title

        self.driver.save_screenshot("login_success.png")

    def test_wrong_password(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.set_email("admin@phptravels.com")
        login_page.set_password("12345")
        login_page.login_fail_button_click()

        error_msg = login_page.get_error_message()
        self.assertEquals(error_msg.text, "Invalid Login Credentials")

        self.driver.save_screenshot("login_fail_wrong_password.png")

    def test_wrong_email(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.set_email("wrong@email.com")
        login_page.set_password("demoadmin")
        login_page.login_fail_button_click()

        error_msg = login_page.get_error_message()
        self.assertEquals(error_msg.text, "Invalid Login Credentials")

    def test_empty_fields(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.set_email("")
        login_page.set_password("")
        login_page.login_empty_button_click()

        assert "dashboard" not in self.driver.title

        self.driver.save_screenshot("login_fail_empty_fields.png")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
