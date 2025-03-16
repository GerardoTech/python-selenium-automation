from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_EMPTY_TEXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(*CART_EMPTY_TEXT).text
    assert expected_result == actual_result, f'Expected {expected_result} did no match actual {actual_result}'