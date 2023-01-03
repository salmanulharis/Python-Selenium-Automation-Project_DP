from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
from testrail import *
import time

from Pages.discountRulePage import DiscountRulePage
from Pages.productPage import ProductPage
from Pages.cartPage import CartPage
from Pages.loginPage import LoginPage

class GeneralPropertiesTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()
		cls.client = APIClient('https://zennode.testrail.io/')
		cls.client.user = 'litty@zennode.com'
		cls.client.password = 'QA#INDIAZEN@NELLI'
		

	def test01_login_valid(self):
		driver = self.driver
		client = self.client
		driver.get('http://localhost/automation/wp-login.php')
		login = LoginPage(driver)
		login.enter_username("groot")
		login.enter_password("password")
		login.click_login()


	def test02_field_label(self):
		driver = self.driver
		case = self.client.send_get('get_case/1010958')

		# add discount rule
		driver.get('http://localhost/automation/wp-admin/admin.php?page=thwdpf_settings')
		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		discountRule.click_add_new_rule()
		discountRule.enter_label(case['custom_label'].strip())
		discountRule.enter_discount_amount(case['custom_discount_amount'].strip())
		discountRule.enter_start_date(case['custom_start_date'].strip())
		discountRule.enter_start_time(case['custom_start_time'].strip())
		discountRule.enter_end_date("Jan 31 2023")
		discountRule.enter_end_time(case['custom_end_time'].strip())
		discountRule.click_save_and_close()
		discountRule.check_discount_rule_added()

		#clear cart
		driver.get('http://localhost/automation/cart/')
		cart = CartPage(driver)
		cart.clear_cart()

		# add product to cart
		driver.get('http://localhost/automation/product/belt/')
		product = ProductPage(driver)
		product.click_add_to_cart()
		product.check_product_added_to_cart()
		sale_price = product.get_sale_price()

		# check discount in cart page
		driver.get('http://localhost/automation/cart/')
		msg = "The discount will be applied to the particular product."
		cart.check_amount_discount('default', case['custom_discount_amount'].strip(), sale_price, msg=msg)


	def test03_discount_no_label(self):
		driver = self.driver
		driver.get('http://localhost/automation/wp-admin/admin.php?page=thwdpf_settings')

		# add discount rule test with no label
		discountRule = DiscountRulePage(driver)
		discountRule.click_add_new_rule()
		discountRule.click_save_and_close()
		discountRule.check_label_required_error()


	def test04_fixed_discount(self):
		driver = self.driver
		case = self.client.send_get('get_case/1010961')

		# add discount rule
		driver.get('http://localhost/automation/wp-admin/admin.php?page=thwdpf_settings')
		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		discountRule.click_add_new_rule()
		discountRule.enter_label(case['custom_label'].strip())
		discountRule.select_method(case['custom_method'].strip())
		discountRule.select_discount_type(case['custom_discount_type'].strip())
		discountRule.enter_discount_amount(case['custom_discount_amount'].strip())
		discountRule.enter_start_date(case['custom_start_date'].strip())
		discountRule.enter_start_time(case['custom_start_time'].strip())
		discountRule.enter_end_date("Jan 31 2023")
		discountRule.enter_end_time(case['custom_end_time'].strip())
		discountRule.click_save_and_close()
		discountRule.check_discount_rule_added()

		#clear cart
		driver.get('http://localhost/automation/cart/')
		cart = CartPage(driver)
		cart.clear_cart()

		# add product to cart
		driver.get('http://localhost/automation/product/belt/')
		product = ProductPage(driver)
		product.click_add_to_cart()
		product.check_product_added_to_cart()
		sale_price = product.get_sale_price()

		# check discount in cart page
		driver.get('http://localhost/automation/cart/')
		msg = "The discount will be applied to the particular product as a simple discount."
		cart.check_amount_discount(case['custom_discount_type'].strip(), case['custom_discount_amount'].strip(), sale_price, msg=msg)

	def test05_percentage_discount(self):
		driver = self.driver
		case = self.client.send_get('get_case/1010968')

		# add discount rule
		driver.get('http://localhost/automation/wp-admin/admin.php?page=thwdpf_settings')
		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		discountRule.click_add_new_rule()
		discountRule.enter_label(case['custom_label'].strip())
		discountRule.select_method(case['custom_method'].strip())
		discountRule.select_discount_type(case['custom_discount_type'].strip())
		discountRule.enter_discount_amount(case['custom_discount_amount'].strip())
		discountRule.enter_start_date(case['custom_start_date'].strip())
		discountRule.enter_start_time(case['custom_start_time'].strip())
		discountRule.enter_end_date("Jan 31 2023")
		discountRule.enter_end_time(case['custom_end_time'].strip())
		discountRule.click_save_and_close()
		discountRule.check_discount_rule_added()

		#clear cart
		driver.get('http://localhost/automation/cart/')
		cart = CartPage(driver)
		cart.clear_cart()

		# add product to cart
		driver.get('http://localhost/automation/product/belt/')
		product = ProductPage(driver)
		product.click_add_to_cart()
		product.check_product_added_to_cart()
		sale_price = product.get_sale_price()

		# check discount in cart page
		driver.get('http://localhost/automation/cart/')
		msg = "The discount will be applied to the particular product as a percentage discount."
		cart.check_amount_discount(case['custom_discount_type'].strip(), case['custom_discount_amount'].strip(), sale_price, msg=msg)


	def test06_valid_discount_amount(self):
		driver = self.driver
		case = self.client.send_get('get_case/1010969')

		# add discount rule
		driver.get('http://localhost/automation/wp-admin/admin.php?page=thwdpf_settings')
		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		discountRule.click_add_new_rule()
		discountRule.enter_label(case['custom_label'].strip())
		discountRule.select_method(case['custom_method'].strip())
		discountRule.select_discount_type(case['custom_discount_type'].strip())
		discountRule.enter_discount_amount(case['custom_discount_amount'].strip())
		discountRule.enter_start_date(case['custom_start_date'].strip())
		discountRule.enter_start_time(case['custom_start_time'].strip())
		discountRule.enter_end_date("Jan 31 2023")
		discountRule.enter_end_time(case['custom_end_time'].strip())
		discountRule.click_save_and_close()
		discountRule.check_discount_rule_added()

		#clear cart
		driver.get('http://localhost/automation/cart/')
		cart = CartPage(driver)
		cart.clear_cart()

		# add product to cart
		driver.get('http://localhost/automation/product/belt/')
		product = ProductPage(driver)
		product.click_add_to_cart()
		product.check_product_added_to_cart()
		sale_price = product.get_sale_price()

		# check discount in cart page
		driver.get('http://localhost/automation/cart/')
		msg = "The discount will be applied to the particular product as a simple discount."
		cart.check_amount_discount(case['custom_discount_type'].strip(), case['custom_discount_amount'].strip(), sale_price, msg=msg)


	def test07_invalid_discount_amount(self):
		driver = self.driver
		case = self.client.send_get('get_case/1010970')

		# add discount rule
		driver.get('http://localhost/automation/wp-admin/admin.php?page=thwdpf_settings')
		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		discountRule.click_add_new_rule()
		discountRule.enter_label(case['custom_label'].strip())
		discountRule.select_method(case['custom_method'].strip())
		discountRule.enter_discount_amount(case['custom_discount_amount'].strip())
		discountRule.click_save_and_close()
		discountRule.check_discount_amount_validation()


	def test08_min_max_qty_valid(self):
		driver = self.driver
		case = self.client.send_get('get_case/1010971')

		# add discount rule
		driver.get('http://localhost/automation/wp-admin/admin.php?page=thwdpf_settings')
		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		discountRule.click_add_new_rule()
		discountRule.enter_label(case['custom_label'].strip())
		discountRule.select_method(case['custom_method'].strip())
		discountRule.enter_min_qty(case['custom_min_qty'].strip())
		discountRule.enter_max_qty(case['custom_max_qty'].strip())
		discountRule.enter_rage_discount(case['custom_amount'].strip())
		discountRule.enter_start_date(case['custom_start_date'].strip())
		discountRule.enter_start_time(case['custom_start_time'].strip())
		discountRule.enter_end_date("Jan 31 2023")
		discountRule.enter_end_time(case['custom_end_time'].strip())
		discountRule.click_save_and_close()
		discountRule.check_discount_rule_added()

		#clear cart
		driver.get('http://localhost/automation/cart/')
		cart = CartPage(driver)
		cart.clear_cart()

		# add product to cart
		driver.get('http://localhost/automation/product/sunglasses/')
		product = ProductPage(driver)
		product.edit_product_quantity(4)
		product.click_add_to_cart()
		product.check_product_added_to_cart()
		sale_price = product.get_sale_price()

		# check discount in cart page
		driver.get('http://localhost/automation/cart/')
		msg = "The discount will be applied to the particular product as a simple discount."
		cart.check_amount_discount('default', case['custom_amount'].strip(), sale_price, msg=msg)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test Complete");


if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))