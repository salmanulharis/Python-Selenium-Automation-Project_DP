from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
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

	def test01_login_valid(self):
		driver = self.driver
		driver.get('http://localhost/automation/wp-login.php')
		login = LoginPage(driver)
		login.enter_username("groot")
		login.enter_password("password")
		login.click_login()


	def test02_create_discount(self):
		driver = self.driver
		driver.get('http://localhost/automation/wp-admin/admin.php?page=thwdpf_settings')

		# add discount rule test
		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		discountRule.click_add_new_rule()
		discountRule.enter_label("Test discount 12")
		discountRule.enter_discount_amount("50")
		discountRule.enter_start_date("Jul 01 2022")
		discountRule.enter_start_time("00:30")
		discountRule.enter_end_date("Dec 31 2022")
		discountRule.enter_end_time("23:30")
		discountRule.click_save_and_close()
		discountRule.check_discount_rule_added()

	def test03_discount_applied(self):
		driver = self.driver
		driver.get('http://localhost/automation/product/belt/')

		# add product to cart
		product = ProductPage(driver)
		product.click_add_to_cart()
		product.check_product_added_to_cart()
		sale_price = product.get_sale_price()

		# check discount in cart page
		driver.get('http://localhost/automation/cart/')
		cart = CartPage(driver)
		cart.check_amount_discount("50", sale_price)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test Complete");

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))