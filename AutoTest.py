import unittest

from selenium import webdriver

import TestSite


class AutoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/lukaszsack/downloads/chromedriver')
        TestSite.TestSite.open_site(self)

    def test_button_by_id(self):
        TestSite.TestSite.click_button_by_id(self)
        assert "Button success" in self.driver.title

    def test_button_by_class_name(self):
        TestSite.TestSite.click_button_by_class_name(self)
        assert "Button success" in self.driver.title

    def test_button_by_name(self):
        TestSite.TestSite.click_button_by_name(self)
        assert "Button success" in self.driver.title

    def test_click_me_button(self):
        TestSite.TestSite.click_me_button(self)

    def test_click_link(self):
        TestSite.TestSite.click_link(self)

    def test_form(self):
        form_test = TestSite.TestSite(self.driver)
        form_test.set_name("John")
        form_test.set_email("email@example.com")
        form_test.click_form_button()

        self.assertEquals(form_test.form_error_assert().text,
                          "email: Email address blocked. Please refer to https://help.aweber.com/entries/97662366 .")

    def test_random_radio_button(self):
        TestSite.TestSite.radio_buttons(self)

    def test_open_toggle(self):
        TestSite.TestSite.open_toggle(self)
        self.assertEquals(TestSite.TestSite.toggle_message(self).text, "Automation testing is awesome")

    def test_tab(self):
        test_tab = TestSite.TestSite(self.driver)
        test_tab.click_tab_2()
        self.assertEquals(test_tab.tab_2_msg_assert().text, "This is tab 2")

        test_tab.click_tab_1()
        self.assertEquals(test_tab.tab_1_msg_assert().text, "This is tab 1")

    def test_checkbox(self):
        TestSite.TestSite.click_checkbox(self)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
