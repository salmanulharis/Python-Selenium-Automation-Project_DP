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

class DiscountRuleTest(unittest.TestCase):

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


	def test02_create_discount(self):
		driver = self.driver
		driver.get('http://localhost/automation/wp-admin/admin.php?page=thwdpf_settings')
		case = self.client.send_get('get_case/1010958')

		# add discount rule test
		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		discountRule.click_add_new_rule()
		discountRule.enter_label(case['custom_label'].strip())
		discountRule.enter_discount_amount(case['custom_discount_amount'].strip())
		discountRule.enter_start_date(case['custom_start_date'].strip())
		discountRule.enter_start_time(case['custom_start_time'].strip())
		discountRule.enter_end_date("Dec 31 2022")
		discountRule.enter_end_time(case['custom_end_time'].strip())
		discountRule.click_save_and_close()
		discountRule.check_discount_rule_added()

	def test03_discount_applied(self):
		driver = self.driver
		driver.get('http://localhost/automation/product/belt/')
		case = self.client.send_get('get_case/1010958')

		# add product to cart
		product = ProductPage(driver)
		product.click_add_to_cart()
		product.check_product_added_to_cart()
		sale_price = product.get_sale_price()

		# check discount in cart page
		driver.get('http://localhost/automation/cart/')
		cart = CartPage(driver)
		cart.check_amount_discount(case['custom_discount_amount'].strip(), sale_price)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test Complete");

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))