from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")


@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    expected_text = 'tea'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'



