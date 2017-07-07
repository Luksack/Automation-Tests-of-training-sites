from selenium.webdriver.common.by import By
from selenium import webdriver

class go_to_page(object):
    url = None

    def __init__(self, driver):
        self.driver = driver
        #driver = webdriver.Chrome(executable_path='/Users/lukaszsack/downloads/chromedriver')
        driver.implicitly_wait(15)

    find_login = (By.NAME, "email")
    find_password = (By.NAME, "password")
    find_login_button = (By.XPATH, "//button [@class = 'btn btn-primary btn-block ladda-button fadeIn animated']")

    def navigate(self):
        self.driver.get(self.url)

class Page_Login(go_to_page):

    def insert_email(self):
        email = "admin@phptravels.com"
        ins_mail = self.driver.find_element(*go_to_page.find_login)
        ins_mail.send_keys(email)

    def insert_password(self):
        password = "demoadmin"
        ins_pass = self.driver.find_element(*go_to_page.find_password)
        ins_pass.send_keys(password)

    def login_button_click(self):
        button_click = self.driver.find_element(*go_to_page.find_login_button)
        button_click.click()