import unittest
import time
from selenium import webdriver

from Flight import FlightPage

class FlightTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/lukaszsack/downloads/chromedriver')
        FlightPage.FlightPage.open_page(self)

    def test_flight_economy_both_ways(self):
        test_flight = FlightPage.FlightPage(self.driver)
        test_flight.set_airport("Berlin")
        test_flight.set_destination("Teneryfa")
        test_flight.set_departure("28 września")
        test_flight.set_return("10 października")
        test_flight.print_flights()

    def test_flight_economy_one_way(self):
        test_flight = FlightPage.FlightPage(self.driver)
        test_flight.one_way_button_click()
        test_flight.set_airport("Berlin")
        test_flight.set_destination("Teneryfa")
        test_flight.set_departure("10 października")
        test_flight.print_flights()

    def test_flight_business_both_ways(self):
        test_flight = FlightPage.FlightPage(self.driver)
        test_flight.set_business_class()
        test_flight.set_airport("Berlin")
        test_flight.set_destination("Teneryfa")
        test_flight.set_departure("28 września")
        test_flight.set_return("10 października")
        test_flight.print_flights()

    def test_flight_business_one_way(self):
        test_flight = FlightPage.FlightPage(self.driver)
        test_flight.one_way_button_click()
        test_flight.set_business_class()
        test_flight.set_airport("Berlin")
        test_flight.set_destination("Teneryfa")
        test_flight.set_departure("28 września")
        test_flight.print_flights()

    def test_flight_detail_info(self):
        test_flight = FlightPage.FlightPage(self.driver)
        test_flight.set_airport("Berlin")
        test_flight.set_destination("Teneryfa")
        test_flight.set_departure("28 września")
        test_flight.set_return("10 października")
        test_flight.details_click()

        first_flight = test_flight.assert_flight_1()
        self.assertEquals(first_flight.text, "Berlin (SXF) – Teneryfa (TFS)")









    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
