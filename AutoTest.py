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
        Name = "John Doe"
        Email = "Email@email.com"
        Tab = "//*[@id='post-5969']/div/div[3]/div/div[2]/div[4]/ul"
        wait = WebDriverWait(driver, 10)

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

        driver.find_element(By.ID, "et_pb_signup_firstname").send_keys(Name)
        driver.find_element(By.ID, "et_pb_signup_email").send_keys(Email)
        driver.find_element(By.CLASS_NAME, "et_pb_newsletter_button").click()

        error = wait.until(EC.visibility_of_element_located((By.XPATH, "//div [@class = 'et_pb_newsletter_result']")))
        self.assertEquals(error.text,
                          "email: Email address blocked. Please refer to https://help.aweber.com/entries/97662366 .")

        options = driver.find_elements(By.XPATH, "//input[@name='selection']")
        option = random.choice(options)
        option.click()

        toggle = driver.find_element(By.CLASS_NAME, "buttonClassExample")
        driver.execute_script("arguments[0].scrollIntoView()", toggle)

        driver.find_element(By.XPATH, "(//h5)[1][@class='et_pb_toggle_title']").click()
        sign = driver.find_element(By.XPATH, "(//div[@class ='et_pb_toggle_content clearfix'])[1]")
        self.assertEquals(sign.text, "Automation testing is awesome")

        driver.find_element(By.XPATH, Tab + '/li[2]/a').click()
        sign2 = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='et_pb_tab clearfix et-pb-active-slide']")))
        self.assertEquals(sign2.text, "This is tab 2")

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'opacity: 1')]")))
        driver.find_element(By.XPATH, Tab + "/li[1]/a").click()
        sign3 = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                             "//div[@class='et_pb_tab clearfix et_pb_active_content et-pb-active-slide']")))
        self.assertEquals(sign3.text, "This is tab 1")

        driver.find_element(By.XPATH, "(//h5)[2][@class = 'et_pb_toggle_title']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type = 'checkbox']")))
        options1 = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
        option = random.choice(options1)
        option.click()

        driver.save_screenshot('Test.png')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
