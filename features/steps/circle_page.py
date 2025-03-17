from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BENEFIT_CELLS = (By.CSS_SELECTOR, ".cell-item-content")


@given('Open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')
    sleep(2)


@then('Verify there are at least 10 benefit cells')
def verify_cell_amount(context):
    cells = context.driver.find_elements(*BENEFIT_CELLS)
    print(f'Found {len(cells)} benefit cells')
    assert len(cells) >= 10, f'Expected at least 10 benefit cells, but got {len(cells)}'