from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

class ProductPage():

	def __init__(self, driver):
		self.driver = driver

		self.add_to_cart_button_xpath = "//button[contains(text(),'Add to cart')]"
		self.added_to_cart_message_xpath = "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]"
		self.striked_sale_price_text_xpath = "//body[1]/div[2]/div[2]/div[1]/div[2]/main[1]/div[2]/div[2]/p[1]/del[1]/span[1]/bdi[1]"
		self.sale_price_text_xpath = "//body[1]/div[2]/div[2]/div[1]/div[2]/main[1]/div[2]/div[2]/p[1]/span[1]/bdi[1]"
		self.quantity_number_name = "quantity"

	def click_add_to_cart(self):
		self.driver.find_element(By.XPATH, self.add_to_cart_button_xpath).click()

	def get_sale_price(self):
		element = self.driver.find_element(By.XPATH, self.striked_sale_price_text_xpath)
		sale_price = element.text[1:]
		return sale_price


	def check_product_added_to_cart(self):
		wc_message = self.driver.find_element(By.XPATH, self.added_to_cart_message_xpath).text
		if len(wc_message) > 0:
			print("Product added to cart successfully.")
		else:
			raise Exception("Product not added to cart.")

	def edit_product_quantity(self, count):
		self.driver.find_element(By.NAME, self.quantity_number_name).clear()
		self.driver.find_element(By.NAME, self.quantity_number_name).send_keys(count)

