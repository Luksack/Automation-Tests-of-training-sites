import unittest
from selenium import webdriver
from Ecommerce import EcommercePage


class EcommerceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/lukaszsack/Downloads/chromedriver')
        self.driver.maximize_window()
        EcommercePage.EcommercePage.open_page(self)

    def test_search_multi_items(self):
        query = "dress"
        ecommerce = EcommercePage.EcommercePage(self.driver)
        ecommerce.set_query(query)
        ecommerce.get_html_list()

        list_assert = ecommerce.assert_list()
        self.assertEqual(list_assert.text, (str(ecommerce.get_html_list()) + " results have been found."))
        query_assert = ecommerce.assert_query()
        self.assertEqual(query_assert.text, '"{}"'.format(query.upper()))

    def test_search_single_item(self):
        query = "shirt"
        ecommerce = EcommercePage.EcommercePage(self.driver)
        ecommerce.set_query(query)
        ecommerce.get_html_list()

        list_assert = ecommerce.assert_list()
        self.assertEqual(list_assert.text, (str(ecommerce.get_html_list()) + " result has been found."))
        query_assert = ecommerce.assert_query()
        self.assertEqual(query_assert.text, '"{}"'.format(query.upper()))

    def test_add_product_to_cart(self):
        query = "dress"
        ecommerce = EcommercePage.EcommercePage(self.driver)
        ecommerce.set_query(query)
        ecommerce.get_product()
        ecommerce.add_to_cart()

        cart_assert = ecommerce.assert_cart()
        self.assertEqual(cart_assert.text, "Product successfully added to your shopping cart")

    def test_create_account(self):
        name = "Robert"
        last_name = "Kozak"
        ecommerce = EcommercePage.EcommercePage(self.driver)
        ecommerce.sign_in_click()
        ecommerce.set_email("example@example6.com")
        ecommerce.set_gender("male")
        ecommerce.set_name(name)
        ecommerce.set_last_name(last_name)
        ecommerce.set_password("qwert123")
        ecommerce.set_birth_date()
        ecommerce.set_address("300 BOYLSTON AVE E")
        ecommerce.set_state()
        ecommerce.set_city("Boylston")
        ecommerce.set_postal_code("55786")
        ecommerce.set_mobile_phone("456666678")
        ecommerce.register_button()

        create_account_assert = ecommerce.assert_create_account()
        self.assertEqual(create_account_assert.text,name +" "+ last_name)

    def test_login_success(self):
        ecommerce = EcommercePage.EcommercePage(self.driver)
        ecommerce.sign_in_click()
        ecommerce.set_login_mail("example@example6.com")
        ecommerce.set_login_password("qwert123")
        ecommerce.sign_in_button_click()

        login_assert = ecommerce.assert_login_success()
        self.assertEqual(login_assert.text, "MY ACCOUNT")

    def test_login_fail(self):
        ecommerce = EcommercePage.EcommercePage(self.driver)
        ecommerce.sign_in_click()
        ecommerce.set_login_mail("example@example6.com")
        ecommerce.set_login_password("asd123")
        ecommerce.sign_in_button_fail()

        error_assert = ecommerce.assert_login_fail()
        self.assertEqual(error_assert.text, "There is 1 error\nAuthentication failed.")


    def test_product_buy(self):
        query = "dress"
        ecommerce = EcommercePage.EcommercePage(self.driver)
        ecommerce.set_query(query)
        ecommerce.get_product()
        ecommerce.add_to_cart()
        ecommerce.check_out_button_click()
        ecommerce.cart_check_out_button_click()
        ecommerce.set_login_mail("example@example6.com")
        ecommerce.set_login_password("qwert123")
        ecommerce.sign_in_button_click()
        ecommerce.proceed_to_checkout_button_click()
        ecommerce.check_terms()
        ecommerce.shipping_button_click()


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
