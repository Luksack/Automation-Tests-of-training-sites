import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestSite():
    BUTTON_BY_ID = (By.ID, "idExample")
    BUTTON_BY_CLASS_NAME = (By.CLASS_NAME, "buttonClassExample")
    BUTTON_BY_NAME = (By.NAME, "NameExample")
    CLICK_ME_BUTTON = (By.CLASS_NAME, "et_pb_promo_button")
    LINK_CLICK = (By.ID, "simpleElementsLink")
    FORM_NAME = (By.ID, "et_pb_signup_firstname")
    FORM_EMAIL = (By.ID, "et_pb_signup_email")
    FORM_BUTTON = (By.CLASS_NAME, "et_pb_newsletter_button")
    FORM_ERROR = (By.XPATH, "//div [@class = 'et_pb_newsletter_result']")
    RADIO_BUTTONS = (By.XPATH, "//input[@name='selection']")
    SCROLL_UP = (By.CLASS_NAME, "buttonClassExample")
    TOGGLE_EXAMPLE = (By.XPATH, "(//h5)[1][@class='et_pb_toggle_title']")
    TOGGLE_MSG = (By.XPATH, "(//div[@class ='et_pb_toggle_content clearfix'])[1]")
    TAB_2 = (By.XPATH, "//*[@id='post-5969']/div/div[3]/div/div[2]/div[4]/ul/li[2]/a")
    TAB_2_MSG = (By.XPATH, "//div[@class='et_pb_tab clearfix et-pb-active-slide']")
    TAB_2_OPACITY = (By.XPATH, "//div[contains(@style, 'opacity: 1')]")
    TAB_1 = (By.XPATH, "//*[@id='post-5969']/div/div[3]/div/div[2]/div[4]/ul/li[1]/a")
    TAB_1_MSG = (By.XPATH, "//div[@class='et_pb_tab clearfix et_pb_active_content et-pb-active-slide']")
    CHECKBOX_EXAMPLE = (By.XPATH, "(//h5)[2][@class = 'et_pb_toggle_title']")
    CHECKBOX_CHOICE = (By.XPATH, "//input[@type = 'checkbox']")

    def __init__(self, driver):
        self.driver = driver

    def open_site(self):
        self.driver.get("http://www.qtptutorial.net/automation-practice/")

    def click_button_by_id(self):
        button = self.driver.find_element(*TestSite.BUTTON_BY_ID)
        button.click()

    def click_button_by_class_name(self):
        button = self.driver.find_element(*TestSite.BUTTON_BY_CLASS_NAME)
        button.click()

    def click_button_by_name(self):
        button = self.driver.find_element(*TestSite.BUTTON_BY_NAME)
        button.click()

    def click_me_button(self):
        button = self.driver.find_element(*TestSite.CLICK_ME_BUTTON)
        button.click()

    def click_link(self):
        link = self.driver.find_element(*TestSite.LINK_CLICK)
        link.click()

    def set_name(self, name):
        set_name = self.driver.find_element(*TestSite.FORM_NAME)
        set_name.send_keys(name)

    def set_email(self, email):
        set_email = self.driver.find_element(*TestSite.FORM_EMAIL)
        set_email.send_keys(email)

    def click_form_button(self):
        wait = WebDriverWait(self.driver, 10)
        button = self.driver.find_element(*TestSite.FORM_BUTTON)
        button.click()
        wait.until(EC.visibility_of_element_located((TestSite.FORM_ERROR)))

    def form_error_assert(self):
        return self.driver.find_element(*TestSite.FORM_ERROR)

    def radio_buttons(self):
        radio = self.driver.find_elements(*TestSite.RADIO_BUTTONS)
        option = random.choice(radio)
        option.click()

    def open_toggle(self):
        toggle = self.driver.find_element(*TestSite.TOGGLE_EXAMPLE)
        toggle.click()

    def toggle_message(self):
        return self.driver.find_element(*TestSite.TOGGLE_MSG)

    def click_tab_2(self):
        wait = WebDriverWait(self.driver, 10)
        tab = self.driver.find_element(*TestSite.TAB_2)
        tab.click()
        wait.until(EC.visibility_of_element_located((TestSite.TAB_2_MSG)))

    def tab_2_msg_assert(self):
        return self.driver.find_element(*TestSite.TAB_2_MSG)

    def click_tab_1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((TestSite.TAB_2_OPACITY)))
        tab = self.driver.find_element(*TestSite.TAB_1)
        tab.click()
        wait.until(EC.visibility_of_element_located((TestSite.TAB_1_MSG)))

    def tab_1_msg_assert(self):
        return self.driver.find_element(*TestSite.TAB_1_MSG)

    def click_checkbox(self):
        wait = WebDriverWait(self.driver, 10)
        checkbox = self.driver.find_element(*TestSite.CHECKBOX_EXAMPLE)
        checkbox.click()
        wait.until(EC.visibility_of_element_located((TestSite.CHECKBOX_CHOICE)))
        checkbox_select = self.driver.find_elements(*TestSite.CHECKBOX_CHOICE)
        option = random.choice(checkbox_select)
        option.click()
