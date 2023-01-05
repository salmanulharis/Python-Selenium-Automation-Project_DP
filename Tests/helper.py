from Pages.discountRulePage import DiscountRulePage
from Pages.productPage import ProductPage
from Pages.cartPage import CartPage
from Pages.loginPage import LoginPage

class ProductRule():
	def __init__(self, driver):
		self.driver = driver

	def add_new_rule(self, settings_url, case):
		driver = self.driver
		driver.get(settings_url)

		discountRule = DiscountRulePage(driver)
		discountRule.clear_all_discounts()
		driver.refresh()
		discountRule.click_add_new_rule()
		discountRule.enter_label(case['custom_label'].strip())

		discount_method = 'default'
		if case['custom_method']:
			discountRule.select_method(case['custom_method'].strip())
			discount_method = case['custom_method'].strip()

		if discount_method == 'Simple discount' or discount_method == 'default':
			if case['custom_discount_type']:
				discountRule.select_discount_type(case['custom_discount_type'].strip())
			discountRule.enter_discount_amount(case['custom_discount_amount'].strip())
		elif discount_method == 'Bulk discount':
			discountRule.enter_min_qty(case['custom_min_qty'].strip())
			discountRule.enter_max_qty(case['custom_max_qty'].strip())
			if(case['custom_discount_type']):
				discountRule.select_range_discount_type(case['custom_discount_type'].strip())
			discountRule.enter_rage_discount(case['custom_amount'].strip())

		discountRule.enter_start_date(case['custom_start_date'].strip())
		discountRule.enter_start_time(case['custom_start_time'].strip())
		discountRule.enter_end_date("Jan 31 2023")
		discountRule.enter_end_time(case['custom_end_time'].strip())
		discountRule.click_save_and_close()
		discountRule.check_discount_rule_added()

	def check_discount_applied(self, case, cart_url, product_url, quantity=1, msg=''):
		driver = self.driver
		#clear cart
		driver.get(cart_url)
		cart = CartPage(driver)
		cart.clear_cart()

		# add product to cart
		driver.get(product_url)
		product = ProductPage(driver)
		sale_price = product.get_sale_price()
		product.edit_product_quantity(quantity)
		product.click_add_to_cart()
		product.check_product_added_to_cart()
		

		# check discount in cart page
		driver.get(cart_url)
		discount_type = case['custom_discount_type'].strip() if case['custom_discount_type'] else 'default'

		discount_method = 'default'
		if case['custom_method']:
			discount_method = case['custom_method'].strip()
			
		discount = 0
		if discount_method == 'Simple discount' or discount_method == 'default':
			discount = case['custom_discount_amount'].strip()
		elif discount_method == 'Bulk discount':
			discount = case['custom_amount'].strip()


		result_flag = cart.check_amount_discount(discount_type, discount, sale_price, msg=msg)

		return result_flag
