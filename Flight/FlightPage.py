from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
class FlightPage():

    AIRPORT = (By.XPATH, "//input[@tabindex = '1']")
    AIRPORT_CLICK = (By.XPATH, "(//div[@class='EIGTDNC-yb-a'])[1]")
    DESTINATION = (By.XPATH, "//input[@tabindex = '2']")
    DESTINATION_CLICK = (By.XPATH, "(//div[@class='EIGTDNC-yb-a'])[2]")
    DEPARTURE = (By.XPATH, "//input[@tabindex='3']")
    RETURN = (By.XPATH, "//input[@tabindex='4']")

    ONE_WAY_BUTTON = (By.XPATH, "(//button[@type = 'button'])[2]")

    FLIGHT_PRICE = (By.XPATH, "(//div[@class = 'EIGTDNC-d-Ab'])[1]")
    FLIGHT_TIME = (By.XPATH, "(//div[@class = 'EIGTDNC-d-E'])[1]")
    FLIGHT_TRANSFER = (By.XPATH, "(//div[@class = 'EIGTDNC-d-Qb'])[1]")

    PRICES = (By.XPATH, "//div[@class = 'EIGTDNC-l-a']")

    ClASS_SELECT_BUTTON = (By.XPATH, "//div[@class = 'EIGTDNC-c-b EIGTDNC-n-g EIGTDNC-n-l']")
    BUSINESS_CLASS = (By.XPATH, "(//div[@class = 'EIGTDNC-c-v'])[2]")

    FLIGHT_DETAILS_CLICK = (By.XPATH, "//a[@class = 'EIGTDNC-d-X EIGTDNC-d-t']")
    DETAILS_WAIT = (By.XPATH, "//div[@class = 'EIGTDNC-Bb-b EIGTDNC-Bb-i']")
    ASSERT_FIRST_FLIGHT = (By.XPATH, "(//div[@class = 'EIGTDNC-d-Kb'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://www.google.pl/flights/")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((FlightPage.DESTINATION)))

    def set_airport(self, airport):
        airport_click = self.driver.find_element(*FlightPage.AIRPORT_CLICK)
        airport_click.click()
        air = self.driver.find_element(*FlightPage.AIRPORT)
        air.clear()
        air.send_keys(airport)

    def set_destination(self, destination):
        destination_click = self.driver.find_element(*FlightPage.DESTINATION_CLICK)
        destination_click.click()
        form = self.driver.find_element(*FlightPage.DESTINATION)
        form.send_keys(destination)
        form.send_keys(Keys.ENTER)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((FlightPage.PRICES)))

    def set_departure(self, date):
        departure = self.driver.find_element(*FlightPage.DEPARTURE)
        departure.clear()
        departure.send_keys(date)
        departure.send_keys(Keys.ENTER)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((FlightPage.PRICES)))

    def set_return(self, date):
        return_date = self.driver.find_element(*FlightPage.RETURN)
        return_date.clear()
        return_date.send_keys(date)
        return_date.send_keys(Keys.ENTER)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((FlightPage.PRICES)))
        self.driver.implicitly_wait(10)

    def print_flights(self):
        price = self.driver.find_element(*FlightPage.FLIGHT_PRICE)
        print(price.text)
        time = self.driver.find_element(*FlightPage.FLIGHT_TIME)
        print(time.text)
        transfer = self.driver.find_element(*FlightPage.FLIGHT_TRANSFER)
        print(transfer.text)

    def one_way_button_click(self):
        button = self.driver.find_element(*FlightPage.ONE_WAY_BUTTON)
        button.click()

    def set_business_class(self):
        button = self.driver.find_element(*FlightPage.ClASS_SELECT_BUTTON)
        button.click()
        business = self.driver.find_element(*FlightPage.BUSINESS_CLASS)
        business.click()

    def details_click(self):
        details = self.driver.find_element(*FlightPage.FLIGHT_DETAILS_CLICK)
        details.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((FlightPage.DETAILS_WAIT)))

    def assert_flight_1(self):
        return self.driver.find_element(*FlightPage.ASSERT_FIRST_FLIGHT)

