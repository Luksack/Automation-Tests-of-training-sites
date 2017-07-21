import unittest

from selenium import webdriver

from SearchTest_Github import SearchPage


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/lukaszsack/downloads/chromedriver')
        SearchPage.SearchPage.open_page(self)

    def test_tour_search_success(self):
        tour_search = SearchPage.SearchPage(self.driver)
        tour_search.tab_click()
        tour_search.location_field_click()
        tour_search.set_location("Dubai")
        tour_search.set_date("23/07/2017")
        tour_search.set_tour_type("Private")
        tour_search.search_tour_button_click()

        assert_msg = tour_search.search_assert_success()
        self.assertEquals(assert_msg.text, "Big Bus Tour of Dubai")

    def test_tour_search_no_results(self):
        tour_search = SearchPage.SearchPage(self.driver)
        tour_search.tab_click()
        tour_search.location_field_click()
        tour_search.set_location("Alexandria")
        tour_search.set_date("19/07/2017")
        tour_search.set_tour_type("Staff training")
        tour_search.search_tour_button_click()

        assert_msg = tour_search.search_assert_no_results()
        self.assertEquals(assert_msg.text, "No Results!!")

    def test_hotel_search_success(self):
        hotel_search = SearchPage.SearchPage(self.driver)
        hotel_search.hotel_location_field_click()
        hotel_search.set_hotel_location("Dubai")
        hotel_search.set_check_in_date("23/07/2017")
        hotel_search.set_check_out_date("30/07/2017")
        hotel_search.search_hotel_button_click()

        assert_msg = hotel_search.hotel_search_assert_success()
        self.assertEquals(assert_msg.text, "Hyatt Regency Perth")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
