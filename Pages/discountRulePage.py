from selenium.webdriver.common.by import By

class DiscountRulePage():

	def __init__(self, driver):
		self.driver = driver

		self.add_new_rule_button_name = "add_rules"
		self.label_textbox_name = "i_label"
		self.discount_amount_textbox_name = "i_discount_amount"
		self.start_date_textbox_name = "i_start_date"
		self.start_time_textbox_name = "i_start_time"
		self.end_date_textbox_name = "i_end_date"
		self.end_time_textbox_name = "i_end_time"
		self.save_and_close_button_xpath = "//span[contains(text(),'Save & Close')]"
		self.discount_rule_added_notice_xpath = "//p[contains(text(),'New discount rule added successfully.')]"
		self.select_all_checkbox_name = "select_all"
		self.delete_button_name = "delete_rules"

	def click_add_new_rule(self):
		self.driver.find_element(By.NAME, self.add_new_rule_button_name).click()

	def enter_label(self, input_value_1):
		self.driver.find_element(By.NAME, self.label_textbox_name).clear()
		self.driver.find_element(By.NAME, self.label_textbox_name).send_keys(input_value_1)

	def enter_discount_amount(self, input_value_2):
		self.driver.find_element(By.NAME, self.discount_amount_textbox_name).clear()
		self.driver.find_element(By.NAME, self.discount_amount_textbox_name).send_keys(input_value_2)

	def enter_start_date(self, input_value_3):
		self.driver.find_element(By.NAME, self.start_date_textbox_name).clear()
		self.driver.find_element(By.NAME, self.start_date_textbox_name).send_keys(input_value_3)

	def enter_start_time(self, input_value_4):
		self.driver.find_element(By.NAME, self.start_time_textbox_name).clear()
		self.driver.find_element(By.NAME, self.start_time_textbox_name).send_keys(input_value_4)

	def enter_end_date(self, input_value_5):
		self.driver.find_element(By.NAME, self.end_date_textbox_name).clear()
		self.driver.find_element(By.NAME, self.end_date_textbox_name).send_keys(input_value_5)

	def enter_end_time(self, input_value_6):
		self.driver.find_element(By.NAME, self.end_time_textbox_name).clear()
		self.driver.find_element(By.NAME, self.end_time_textbox_name).send_keys(input_value_6)

	def click_save_and_close(self):
		self.driver.find_element(By.XPATH, self.save_and_close_button_xpath).click()

	def check_discount_rule_added(self):
		notice = self.driver.find_element(By.XPATH, self.discount_rule_added_notice_xpath).text
		if len(notice):
			print("The discount will be created successfully.")
		else:
			raise Exception("Error: Discount rule not created.")

	def clear_all_discounts(self):
		self.driver.find_element(By.NAME, self.select_all_checkbox_name).click()
		self.driver.find_element(By.NAME, self.delete_button_name).click()
		alert = self.driver.switch_to.alert
		alert.accept()








