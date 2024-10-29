from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In form opened')
def verify_sign_in(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".sc-fe064f5c-0.sc-315b8ab9-2.WObnm.gClYfs").text
    expected_result = 'Sign into your Target account'
    assert expected_result in actual_result, f'Expected {expected_result}, got {actual_result}'

