from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Locators
CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
RESULTS_HEADING = (By.CSS_SELECTOR, "div.h-display-flex[data-test='resultsHeading']")


@then('Verify that correct search results shown for {product}')
def verify_results(context, product):
    actual_result = context.driver.find_element(*RESULTS_HEADING).text
    assert product in actual_result, f'Expected {product}, got {actual_result}'


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"