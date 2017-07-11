from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class LoginPage():
    find_login = (By.NAME, "email")
    find_password = (By.NAME, "password")
    find_login_button = (By.XPATH, "//button [@class = 'btn btn-primary btn-block ladda-button fadeIn animated']")
    find_fail_msg = (By.XPATH, "//div [@class = 'alert alert-danger loading wow fadeIn animated animated']")

    def __init__(self, driver):
        self.driver = driver

    def insert_email(self, email):
        ins_mail = self.driver.find_element(*LoginPage.find_login)
        ins_mail.send_keys(email)

    def insert_password(self, password):
        ins_pass = self.driver.find_element(*LoginPage.find_password)
        ins_pass.send_keys(password)

    def login_success_button_click(self):
        wait = WebDriverWait(self.driver, 10)
        button_click = self.driver.find_element(*LoginPage.find_login_button)
        button_click.click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//a [@class = 'navbar-brand']")))

    def login_fail_button_click(self):
        wait = WebDriverWait(self.driver, 10)
        button_click = self.driver.find_element(*LoginPage.find_login_button)
        button_click.click()
        wait.until(EC.visibility_of_element_located
                   ((By.XPATH,
                        "//div [@class = 'alert alert-danger loading wow fadeIn animated animated']")))

    def login_empty_button_click(self):
        button_click = self.driver.find_element(*LoginPage.find_login_button)
        button_click.click()