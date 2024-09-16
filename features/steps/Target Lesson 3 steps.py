from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href*='cart?prehydrateClick=true']").click()
    sleep(5)

@then("Verify Your cart is empty message is shown")
def verify_cart_is_empty(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    expected_result = 'Your cart is empty'
    assert expected_result in actual_result, f'Expected {expexted_result}, got {actual_result}'

@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(5)

@when('From right side navigation menu, click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(5)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".sc-fe064f5c-0.sc-315b8ab9-2.WObnm.gClYfs").text
    expected_result = 'Sign into your Target account'
    assert expected_result in actual_result, f'Expected {expexted_result}, got {actual_result}'
