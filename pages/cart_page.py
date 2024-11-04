from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    CART_SUMMARY = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    def verify_cart_empty(self):
        actual_result = self.driver.find_element(*self.CART_SUMMARY).text
        expected_result = 'Your cart is empty'
        assert expected_result in actual_result, f'Expected {expected_result}, got {actual_result}'
