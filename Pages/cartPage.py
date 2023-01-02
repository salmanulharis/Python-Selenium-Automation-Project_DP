from selenium.webdriver.common.by import By

class CartPage():

	def __init__(self, driver):
		self.driver = driver

		self.product_price_text_xpath = "//body[1]/div[2]/div[2]/div[1]/div[2]/main[1]/article[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[4]/ins[1]/span[1]/bdi[1]"

	def check_amount_discount(self, discount_type, discount_amount=0, sale_price=0, msg=""):
		cart_price = self.driver.find_element(By.XPATH, self.product_price_text_xpath).text
		cart_price = cart_price[1:]
		discount_price = sale_price

		if discount_amount and sale_price:
			if discount_type == 'Fixed discount' or discount_type == 'default':
				discount_price = float(sale_price) - float(discount_amount)
			elif discount_type == 'Percentage discount':
				discount_price = float(sale_price) * (float(discount_amount)/100)
		print(sale_price)
		print(discount_price)
		print(cart_price)
		if discount_price == float(cart_price):
			if msg:
				print(msg)
			else:
				print("Discount added succesfully.")

		else:
			raise Exception("Discount is not applied.")