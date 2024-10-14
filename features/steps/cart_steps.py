from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click add item to shopping cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()


@when('Confirm add to cart button')
def click_confirm_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='shippingButton'] [id*='addToCartButton']").click()
    sleep(5)


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()


@then("Verify correct item is in shopping cart")
def verify_item_in_cart(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.h-margin-b-tight.h-text-grayDark").text
    expected_result = '1 item'
    assert expected_result in actual_result, f'Expected {expected_result}, got {actual_result}'


@then("Verify Your cart is empty message is shown")
def verify_cart_is_empty(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    expected_result = 'Your cart is empty'
    assert expected_result in actual_result, f'Expected {expected_result}, got {actual_result}'
