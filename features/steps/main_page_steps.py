from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


CART_ITEM_TITLE = (By.CSS_SELECTOR, "div.h-margin-b-tight.h-text-grayDark")
CART_BTN = (By.CSS_SELECTOR, "[href*='cart?prehydrateClick=true']")
SEARCH_BAR = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
SIGN_IN_NAV = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")


@given('Open Target main page')
def open_main(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()

@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart()


@when('Search for {item}')
def search_for_product(context, item):
   context.app.header.search_product(item)


@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_LINK).click()
    # Replacing sleep with WebDriverWait to wait for the side navigation menu
    context.driver.wait.until(
        EC.visibility_of_element_located(SIGN_IN_NAV),
        message='Sign in option not visible in side navigation'
    )


@when('From right side navigation menu, click Sign In')
def click_sign_in_nav(context):
    context.driver.find_element(*SIGN_IN_NAV).click()
    # Adding WebDriverWait to confirm sign-in form visibility
    context.driver.wait.until(
        EC.visibility_of_element_located(SIGN_IN_NAV),
        message='Sign in form not visible after clicking Sign In'
    )