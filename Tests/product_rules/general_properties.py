from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
from testrail import *
import time
import os
from dotenv import load_dotenv

from Pages.discountRulePage import DiscountRulePage
from Pages.productPage import ProductPage
from Pages.cartPage import CartPage
from Pages.loginPage import LoginPage
from helper import get_client, get_test_run_id, update_test_run
from Tests.helper import ProductRule

load_dotenv()

class GeneralPropertiesTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()
		cls.client = get_client()
		cls.test_run_id = 9910
		# cls.test_run_id = get_test_run_id('WDDPF')
		cls.settings_url = os.getenv('WEBSITE_URL') + "/wp-admin/admin.php?page=thwdpf_settings"
		cls.cart_url = os.getenv('WEBSITE_URL') + "/cart/"
		cls.product_url = os.getenv('WEBSITE_URL') + "/product/sunglasses/"
		

	def test01_login_valid(self):
		driver = self.driver
		login_url = os.getenv('WEBSITE_URL') + '/wp-login.php'

		driver.get(login_url)
		login = LoginPage(driver)
		login.enter_username(os.getenv('SITE_USERNAME'))
		login.enter_password(os.getenv('SITE_PASSWORD'))
		login.click_login()
		

	@unittest.skip
	def test02_field_label(self):
		driver = self.driver
		case_id = 1010958
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url
		cart_url = self.cart_url
		product_url = self.product_url

		msg = "The discount will be applied to the particular product."
		product_rule = ProductRule(driver)
		product_rule.add_new_rule(settings_url, case) # add discount rule
		result_flag = product_rule.check_discount_applied(case, cart_url, product_url, msg=msg) #chech discount applied
		
		update_test_run(case_id, run_id, result_flag, msg)


	@unittest.skip
	def test03_discount_no_label(self):
		driver = self.driver
		case_id = 1010960
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url

		# add discount rule test with no label
		driver.get(settings_url)
		discountRule = DiscountRulePage(driver)
		discountRule.click_add_new_rule()
		discountRule.click_save_and_close()
		result_flag = discountRule.check_label_required_error()
		msg = "A validation message will be displayed on top[ that 'Label is required.'"
		update_test_run(case_id, run_id, result_flag, msg)

	@unittest.skip
	def test04_fixed_discount(self):
		driver = self.driver
		case_id = 1010961
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url
		cart_url = self.cart_url
		product_url = self.product_url

		msg = "The discount will be applied to the particular product as a simple discount."
		product_rule = ProductRule(driver)
		product_rule.add_new_rule(settings_url, case) # add discount rule
		result_flag = product_rule.check_discount_applied(case, cart_url, product_url, msg=msg) #chech discount applied

		update_test_run(case_id, run_id, result_flag, msg)

	@unittest.skip
	def test05_percentage_discount(self):
		driver = self.driver
		case_id = 1010968
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url
		cart_url = self.cart_url
		product_url = self.product_url

		msg = "The discount will be applied to the particular product as a percentage discount."
		product_rule = ProductRule(driver)
		product_rule.add_new_rule(settings_url, case) # add discount rule
		result_flag = product_rule.check_discount_applied(case, cart_url, product_url, msg=msg) #chech discount applied

		update_test_run(case_id, run_id, result_flag, msg)

	@unittest.skip
	def test06_valid_discount_amount(self):
		driver = self.driver
		case_id = 1010969
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url
		cart_url = self.cart_url
		product_url = self.product_url

		msg = "The discount will be applied to the particular product as a simple discount."
		product_rule = ProductRule(driver)
		product_rule.add_new_rule(settings_url, case) # add discount rule
		result_flag = product_rule.check_discount_applied(case, cart_url, product_url, msg=msg) #chech discount applied

		update_test_run(case_id, run_id, result_flag, msg)

	@unittest.skip
	def test07_invalid_discount_amount(self):
		driver = self.driver
		case_id = 1010970
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url

		# add discount rule
		driver.get(settings_url)
		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		driver.refresh()
		discountRule.click_add_new_rule()
		discountRule.enter_label(case['custom_label'].strip())
		discountRule.select_method(case['custom_method'].strip())
		discountRule.enter_discount_amount(case['custom_discount_amount'].strip())
		discountRule.click_save_and_close()
		msg = "A validation message 'Please provide a numeric value for Discount Amount field' will appear on top of the pop-up."
		result_flag = discountRule.check_discount_amount_validation()
		update_test_run(case_id, run_id, result_flag, msg)

	@unittest.skip
	def test08_min_max_qty_valid(self):
		driver = self.driver
		case_id = 1010971
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url
		cart_url = self.cart_url
		product_url = self.product_url

		msg = "The discount will be applied to the particular product as a simple discount."
		product_rule = ProductRule(driver)
		product_rule.add_new_rule(settings_url, case) # add discount rul
		result_flag = product_rule.check_discount_applied(case, cart_url, product_url, quantity=4, msg=msg) #chech discount applied

		update_test_run(case_id, run_id, result_flag, msg)

	@unittest.skip
	def test09_min_max_qty_invalid(self):
		driver = self.driver
		case_id = 1010973
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url

		# add discount rule
		driver.get(settings_url)
		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		driver.refresh()
		discountRule.click_add_new_rule()
		discountRule.enter_label(case['custom_label'].strip())
		discountRule.select_method(case['custom_method'].strip())
		discountRule.enter_min_qty(case['custom_min_qty'].strip())
		discountRule.click_save_and_close()
		result_flag = discountRule.min_qty_validation()
		msg = "The message 'Invalid pricing range. Please ensure that all the Min. Qty fields have valid values' will be displayed on top of the popup."
		update_test_run(case_id, run_id, result_flag, msg)

	@unittest.skip
	def test10_fixed_range(self):
		driver = self.driver
		case_id = 1010977
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url
		cart_url = self.cart_url
		product_url = self.product_url

		msg = "The discount will be applied to the particular product as a fixed discount."
		product_rule = ProductRule(driver)
		product_rule.add_new_rule(settings_url, case) # add discount rule
		result_flag = product_rule.check_discount_applied(case, cart_url, product_url, quantity=4, msg=msg) #chech discount applied

		update_test_run(case_id, run_id, result_flag, msg)

	@unittest.skip
	def test11_percentage_range(self):
		driver = self.driver
		case_id = 1010979
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url
		cart_url = self.cart_url
		product_url = self.product_url

		msg = "The discount will be applied to the particular product as a percentage discount."
		product_rule = ProductRule(driver)
		product_rule.add_new_rule(settings_url, case) # add discount rule
		result_flag = product_rule.check_discount_applied(case, cart_url, product_url, quantity=4, msg=msg) #chech discount applied

		update_test_run(case_id, run_id, result_flag, msg)

	def test12_bulk_discount_amount_valid(self):
		driver = self.driver
		case_id = 1010980
		run_id = self.test_run_id
		case = self.client.send_get('get_case/%s'%(case_id))
		settings_url = self.settings_url
		cart_url = self.cart_url
		product_url = self.product_url

		msg = "The discount will be applied to the particular product as a simple discount."
		product_rule = ProductRule(driver)
		product_rule.add_new_rule(settings_url, case) # add discount rule
		result_flag = product_rule.check_discount_applied(case, cart_url, product_url, quantity=3, msg=msg) #chech discount applied

		update_test_run(case_id, run_id, result_flag, msg)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test Complete");


if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))