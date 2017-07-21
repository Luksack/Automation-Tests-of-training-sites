from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


class SearchPage():
    TOUR_TAB = (By.XPATH, "//a [@href = '#TOURS'] ")

    TOUR_LOCATION_FIELD = (By.ID, "s2id_autogen5")
    QUERY_FIELD = (By.XPATH, "//*[@id='select2-drop']/div/input")
    LOCATION_PROMPT = (By.XPATH, "//*[@id='select2-drop']/ul/li[1]/ul/li/div")
    HOTEL_LOCATION_FIELD = (By.XPATH, "//*[@id='s2id_autogen3']")
    HOTEL_LOCATION_PROMPT = (By.XPATH, "//*[@id='select2-drop']/ul/li/ul/li[1]")

    CALENDAR_FIELD = (By.XPATH, "//input[@name = 'date']")
    CHECK_IN = (By.XPATH, "//input [@name = 'checkin']")
    CHECK_OUT = (By.XPATH, "//input [@name = 'checkout']")

    TOUR_TYPE = (By.XPATH, "//*[@id='tourtype']")

    SEARCH_TOUR_BUTTON = (By.XPATH, "//*[@id='TOURS']/div/form/div[5]")
    SEARCH_HOTEL_BUTTON = (By.XPATH, "//*[@id='HOTELS']/div/form/div[6]")

    ASSERT_SUCCESS = (By.XPATH, "//*[@id='OVERVIEW']/div/div[2]/div[1]/div[1]/div[1]/div/strong")
    ASSERT_NO_RESULTS = (By.XPATH, "/html/body/div[5]/div[3]/div/h1")
    HOTEL_ASSERT_SUCCES = (By.XPATH, "/html/body/div[5]/div[3]/div/table/tbody/tr[1]/td/div/div[2]/div/div[2]/h4/a")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("http://www.phptravels.net/")

    def tab_click(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((SearchPage.TOUR_TAB)))
        tab = self.driver.find_element(*SearchPage.TOUR_TAB)
        tab.click()

    def location_field_click(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((SearchPage.TOUR_LOCATION_FIELD)))
        field = self.driver.find_element(*SearchPage.TOUR_LOCATION_FIELD)
        field.click()

    def set_location(self, city):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((SearchPage.QUERY_FIELD)))
        location = self.driver.find_element(*SearchPage.QUERY_FIELD)
        location.send_keys(city)
        wait.until(EC.visibility_of_element_located((SearchPage.LOCATION_PROMPT)))
        prompt = self.driver.find_element(*SearchPage.LOCATION_PROMPT)
        prompt.click()

    def set_date(self, date):
        calendar = self.driver.find_element(*SearchPage.CALENDAR_FIELD)
        calendar.click()
        calendar.clear()
        calendar.send_keys(date)

    def set_tour_type(self, type):
        tour = Select(self.driver.find_element(*SearchPage.TOUR_TYPE))
        # options = [o.text for o in tour.options]
        # option = random.choice(options)
        tour.select_by_visible_text(type)

    def search_tour_button_click(self):
        button = self.driver.find_element(*SearchPage.SEARCH_TOUR_BUTTON)
        button.click()

    def search_assert_success(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((SearchPage.ASSERT_SUCCESS)))
        return self.driver.find_element(*SearchPage.ASSERT_SUCCESS)

    def search_assert_no_results(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((SearchPage.ASSERT_NO_RESULTS)))
        return self.driver.find_element(*SearchPage.ASSERT_NO_RESULTS)

    def hotel_location_field_click(self):
        location = self.driver.find_element(*SearchPage.HOTEL_LOCATION_FIELD)
        location.click()

    def set_hotel_location(self, city):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((SearchPage.QUERY_FIELD)))
        location = self.driver.find_element(*SearchPage.QUERY_FIELD)
        location.send_keys(city)
        wait.until(EC.visibility_of_element_located((SearchPage.HOTEL_LOCATION_PROMPT)))
        prompt = self.driver.find_element(*SearchPage.HOTEL_LOCATION_PROMPT)
        prompt.click()

    def set_check_in_date(self, date):
        check_in = self.driver.find_element(*SearchPage.CHECK_IN)
        check_in.clear()
        check_in.send_keys(date)

    def set_check_out_date(self, date):
        check_out = self.driver.find_element(*SearchPage.CHECK_OUT)
        check_out.clear()
        check_out.send_keys(date)

    def hotel_search_assert_success(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((SearchPage.HOTEL_ASSERT_SUCCES)))
        return self.driver.find_element(*SearchPage.HOTEL_ASSERT_SUCCES)

    def search_hotel_button_click(self):
        button = self.driver.find_element(*SearchPage.SEARCH_HOTEL_BUTTON)
        button.click()
