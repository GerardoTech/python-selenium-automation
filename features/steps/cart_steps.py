from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='shippingButton'] [id*='addToCartButton']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "div.h-margin-b-tight.h-text-grayDark")
CART_SUMMARY = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")



@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@when('Click add item to shopping cart')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Side navigation product name not visible'
    )


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Confirm add to cart button')
def click_confirm_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
    context.driver.wait.until(
        EC.presence_of_element_located(CART_ITEM_TITLE),
        message='Cart item title not found after adding to cart'
    )


@then("Verify correct item is in shopping cart")
def verify_item_in_cart(context):
    actual_result = context.driver.find_element(*CART_ITEM_TITLE).text
    expected_result = '1 item'
    assert expected_result in actual_result, f'Expected {expected_result}, got {actual_result}'


@then("Verify Your cart is empty message is shown")
def verify_cart_is_empty(context):
    actual_result = context.driver.find_element(*CART_SUMMARY).text
    expected_result = 'Your cart is empty'
    assert expected_result in actual_result, f'Expected {expected_result}, got {actual_result}'


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"