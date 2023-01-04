from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

class CartPage():

	def __init__(self, driver):
		self.driver = driver

		self.product_price_text_xpath = "//body[1]/div[2]/div[2]/div[1]/div[2]/main[1]/article[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[4]/ins[1]/span[1]/bdi[1]"
		self.cart_item_class_name = "cart_item"
		self.remove_button_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/main[1]/article[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/a[1]"

	def check_amount_discount(self, discount_type, discount_amount=0, sale_price=0, msg=""):
		cart_price = self.driver.find_element(By.XPATH, self.product_price_text_xpath).text
		cart_price = cart_price[1:]
		discount_price = sale_price

		if discount_amount and sale_price:
			if discount_type == 'Fixed discount' or discount_type == 'default' or discount_type == 'Fixed':
				discount_price = float(sale_price) - float(discount_amount)
			elif discount_type == 'Percentage discount' or discount_type == 'Percentage':
				discount_price = float(sale_price) - (float(sale_price) * (float(discount_amount)/100))

		print(sale_price)
		print(discount_price)
		print(cart_price)
		
		if discount_price == float(cart_price):
			result_flag = True
			if msg:
				print(msg)
			else:
				print("Discount added succesfully.")

		else:
			result_flag = False
			raise Exception("Discount is not applied.")
		return result_flag

	def clear_cart(self):
		elements = self.driver.find_elements(By.CLASS_NAME, self.cart_item_class_name)
		i = 1
		if len(elements) > 0:
			while i <= len(elements):
				element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.remove_button_xpath)))
				try:
				    element.click()
				    i += 1
				except:
					pass
			# except WebDriverException:
			#     print("Element is not clickable")
