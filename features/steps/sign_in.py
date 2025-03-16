from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN_TEXT = (By.CSS_SELECTOR, "h1[class^='styles_ndsHeading']")


@then("Verify sign in page opens")
def sign_in_form(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(*SIGN_IN_TEXT).text
    assert expected_result == actual_result, f'Expected {expected_result} did no match actual {actual_result}'