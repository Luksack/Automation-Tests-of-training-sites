from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import random


class EcommercePage:
    PAGE_LOAD = (By.XPATH, "//div [@id = 'header_logo']")

    SEARCH = (By.XPATH, "//input [@id = 'search_query_top']")
    ASSERT_SEARCH = (By.XPATH, "// span[@class = 'lighter']")
    HTML_LIST = (By.XPATH, "//ul[@class = 'product_list grid row']/li")
    LIST = (By.XPATH, "//span[@class = 'heading-counter']")

    PRODUCT = (By.XPATH, "(//div[@class= 'product-image-container'])[1]")
    PRODUCT_WAIT = (By.XPATH, "//div[@id = 'image-block']")
    CART_BUTTON = (By.XPATH, "//button[@name = 'Submit']")
    ASSERT_CART = (By.XPATH, "//*[@id='layer_cart']/div[1]/div[1]/h2")

    SIGN_IN = (By.XPATH, "//a[@class = 'login']")
    CREATE_ACC_BUTTON = (By.XPATH, "//button[@id = 'SubmitCreate']")
    EMAIL = (By.XPATH, "//input[@id = 'email_create']")
    SEX_MALE = (By.XPATH, "//input[@id = 'id_gender1']")
    SEX_FEMALE = (By.XPATH, "//input[@id = 'id_gender2']")
    SET_FIRST_NAME = (By.XPATH, "//input[@id = 'customer_firstname']")
    SET_LAST_NAME = (By.XPATH, "//input[@id = 'customer_lastname']")
    SET_PASSWORD = (By.XPATH, "//input[@id = 'passwd']")
    SET_DAY = (By.XPATH, "//select[@id = 'days']")
    SET_MONTH = (By.XPATH, "//select[@id = 'months']")
    SET_YEAR = (By.XPATH, "//select[@id = 'years']")
    SET_ADDRESS = (By.XPATH, "//input[@id = 'address1']")
    SET_CITY = (By.XPATH, "//input[@id = 'city']")
    SET_POSTAL_CODE = (By.XPATH, "//input[@id = 'postcode']")
    SET_STATE = (By.XPATH, "//select[@id = 'id_state']")
    SET_MOBILE_PHONE = (By.XPATH, "//input[@id = 'phone_mobile']")
    REGISTER_BUTTON = (By.XPATH, "//button[@id = 'submitAccount']")
    ACCOUNT_NAME = (By.XPATH, "//a[@class = 'account']")

    LOGIN_MAIL = (By.XPATH, "//input[@id = 'email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@id = 'passwd']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@id = 'SubmitLogin']")
    ASSERT_LOGIN = (By.XPATH, "//h1[@class = 'page-heading']")

    ERROR_MSG = (By.XPATH, "//div[@class = 'alert alert-danger']")

    CHECK_OUT_BUTTON = (By.XPATH, "//a[@class = 'btn btn-default button button-medium']")
    CHECK_OUT_BUTTON_CART = (By.XPATH, "//a[@class = 'button btn btn-default standard-checkout button-medium']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//button[@class = 'button btn btn-default button-medium']")
    TERMS_OF_SERVICE_CHECK = (By.XPATH, "//input[@id = 'cgv']")
    SHIPPING_BUTTON = (By.XPATH,"//button[@class = 'button btn btn-default standard-checkout button-medium']" )
    PAY_BY_BANK = (By.XPATH, "//a[@class = 'bankwire']")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("http://automationpractice.com/index.php")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.PAGE_LOAD)))

    def set_query(self, query):
        search = self.driver.find_element(*EcommercePage.SEARCH)
        search.click()
        search.send_keys(query)
        search.send_keys(Keys.ENTER)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.ASSERT_SEARCH)))

    def assert_query(self):
        return self.driver.find_element(*EcommercePage.ASSERT_SEARCH)

    def get_html_list(self):
        html_list = self.driver.find_elements(*EcommercePage.HTML_LIST)
        list_items = (len(html_list))
        return list_items

    def assert_list(self):
        return self.driver.find_element(*EcommercePage.LIST)

    def get_product(self):
        item = self.driver.find_element(*EcommercePage.PRODUCT)
        item.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.PRODUCT_WAIT)))

    def add_to_cart(self):
        cart_button = self.driver.find_element(*EcommercePage.CART_BUTTON)
        cart_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.ASSERT_CART)))

    def assert_cart(self):
        return self.driver.find_element(*EcommercePage.ASSERT_CART)

    def sign_in_click(self):
        button = self.driver.find_element(*EcommercePage.SIGN_IN)
        button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.CREATE_ACC_BUTTON)))

    def set_email(self, email_address):
        email = self.driver.find_element(*EcommercePage.EMAIL)
        email.send_keys(email_address)
        button = self.driver.find_element(*EcommercePage.CREATE_ACC_BUTTON)
        button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.SEX_MALE)))

    def set_gender(self, sex):

        if sex == "male":
            radio = self.driver.find_element(*EcommercePage.SEX_MALE)
            radio.click()
        elif sex == "female":
            radio1 = self.driver.find_element(*EcommercePage.SEX_FEMALE)
            radio1.click()
        else:
            print("No Sex selected")

    def set_name(self, first_name):
        name = self.driver.find_element(*EcommercePage.SET_FIRST_NAME)
        name.send_keys(first_name)

    def set_last_name(self, last_name):
        name = self.driver.find_element(*EcommercePage.SET_LAST_NAME)
        name.send_keys(last_name)

    def set_password(self, password):
        passw = self.driver.find_element(*EcommercePage.SET_PASSWORD)
        passw.send_keys(password)

    def set_birth_date(self):
        birth_day = Select(self.driver.find_element(*EcommercePage.SET_DAY))
        day_select = [day.text for day in birth_day.options]
        option = random.choice(day_select)
        birth_day.select_by_visible_text(option)

        birth_month = Select(self.driver.find_element(*EcommercePage.SET_MONTH))
        month_select = [month.text for month in birth_month.options]
        option1 = random.choice(month_select)
        birth_month.select_by_visible_text(option1)

        birth_year = Select(self.driver.find_element(*EcommercePage.SET_YEAR))
        year_select = [year.text for year in birth_year.options]
        option2 = random.choice(year_select)
        birth_year.select_by_visible_text(option2)

    def set_address(self, adres):
        address = self.driver.find_element(*EcommercePage.SET_ADDRESS)
        address.send_keys(adres)

    def set_city(self, user_city):
        city = self.driver.find_element(*EcommercePage.SET_CITY)
        city.send_keys(user_city)

    def set_state(self):
        state = Select(self.driver.find_element(*EcommercePage.SET_STATE))
        state_select = [states.text for states in state.options]
        option = random.choice(state_select)
        state.select_by_visible_text(option)

    def set_postal_code(self, postal_code):
        code = self.driver.find_element(*EcommercePage.SET_POSTAL_CODE)
        code.send_keys(postal_code)

    def set_mobile_phone(self, number):
        phone = self.driver.find_element(*EcommercePage.SET_MOBILE_PHONE)
        phone.send_keys(number)

    def register_button(self):
        button = self.driver.find_element(*EcommercePage.REGISTER_BUTTON)
        button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.PAGE_LOAD)))

    def assert_create_account(self):
        return self.driver.find_element(*EcommercePage.ACCOUNT_NAME)

    def set_login_mail(self, email):
        mail = self.driver.find_element(*EcommercePage.LOGIN_MAIL)
        mail.send_keys(email)

    def set_login_password(self, password):
        paswrd = self.driver.find_element(*EcommercePage.LOGIN_PASSWORD)
        paswrd.send_keys(password)

    def sign_in_button_click(self):
        button = self.driver.find_element(*EcommercePage.SIGN_IN_BUTTON)
        button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.ASSERT_LOGIN)))


    def assert_login_success(self):
        return self.driver.find_element(*EcommercePage.ASSERT_LOGIN)

    def sign_in_button_fail(self):
        button = self.driver.find_element(*EcommercePage.SIGN_IN_BUTTON)
        button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.ERROR_MSG)))

    def assert_login_fail(self):
        return self.driver.find_element(*EcommercePage.ERROR_MSG)

    def check_out_button_click(self):
        button = self.driver.find_element(*EcommercePage.CHECK_OUT_BUTTON)
        button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.CHECK_OUT_BUTTON_CART)))
    def cart_check_out_button_click(self):
        button = self.driver.find_element(*EcommercePage.CHECK_OUT_BUTTON_CART)
        button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.SIGN_IN_BUTTON)))
    def proceed_to_checkout_button_click(self):
        button = self.driver.find_element(*EcommercePage.PROCEED_TO_CHECKOUT_BUTTON)
        button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.SHIPPING_BUTTON)))
    def check_terms(self):
        check = self.driver.find_element(*EcommercePage.TERMS_OF_SERVICE_CHECK)
        check.click()
    def shipping_button_click(self):
        button = self.driver.find_element(*EcommercePage.SHIPPING_BUTTON)
        button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((EcommercePage.PAY_BY_BANK)))