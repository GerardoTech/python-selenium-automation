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


@when('Search for a {item}')
def search_for_product(context, item):
    print(item)
    context.driver.find_element(By.ID, 'search').send_keys(item)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(5)


@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(5)


@when('From right side navigation menu, click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(5)