from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify page has {expected_amount} benefits cells')
def verify_page_cells(context, expected_amount):
    expected_amount = int(expected_amount)
    cells = context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")
    print(cells)
    assert len(cells) == expected_amount, f'Expected {expected_amount} cells but got {len(cells)}'
