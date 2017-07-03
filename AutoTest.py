import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutoTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/lukaszsack/downloads/chromedriver')

    def test_auto_site(self):
        driver = self.driver
        driver.get("http://www.qtptutorial.net/automation-practice/")
        assert "Automation Testing Practice Page" in driver.title
        driver.find_element(By.ID, "idExample").click()
        assert "Button success" in driver.title
        driver.back()
        driver.find_element(By.CLASS_NAME, "buttonClassExample").click()
        assert "Button success" in driver.title
        driver.back()
        driver.find_element(By.NAME, "NameExample").click()
        assert "Button success" in driver.title
        driver.back()
        driver.find_element(By.CLASS_NAME, "et_pb_promo_button").click()
        driver.back()
        driver.find_element(By.ID, "simpleElementsLink").click()
        driver.back()
        #driver.find_element(By.XPATH, "//*[@id='post-5969']/div/div[3]/div/div[1]/div[4]/div/h4/a").click()
        driver.find_element(By.ID, "et_pb_signup_firstname").send_keys("John Doe")
        driver.find_element(By.ID, "et_pb_signup_email").send_keys("Email@email.com")
        driver.find_element(By.CLASS_NAME, "et_pb_newsletter_button").click()
        time.sleep(5)
        assert "email: Email address blocked. Please refer to https://help.aweber.com/entries/97662366" in driver.page_source
        #Radio buttons random sellect
        options = driver.find_elements(By.XPATH, "//input[@name='selection']")
        option = random.choice(options)
        option.click()
        toggle = driver.find_element(By.CLASS_NAME, "buttonClassExample")
        driver.execute_script("arguments[0].scrollIntoView()", toggle)
        driver.find_element(By.XPATH, "(//h5)[1][@class='et_pb_toggle_title']").click()
        assert "Automation testing is awesome" in driver.page_source
        driver.find_element(By.XPATH, "//*[@id='post-5969']/div/div[3]/div/div[2]/div[4]/ul/li[2]/a").click()
        assert "This is tab 2" in driver.page_source
        driver.find_element(By.XPATH, "//*[@id='post-5969']/div/div[3]/div/div[2]/div[4]/ul/li[1]/a")
        assert "This is tab 1" in driver.page_source
        driver.find_element(By.XPATH, "(//h5)[2][@class = 'et_pb_toggle_title']").click()
        time.sleep(2)
        options1 = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
        option = random.choice(options1)
        option.click()






        driver.save_screenshot('Test.png')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()