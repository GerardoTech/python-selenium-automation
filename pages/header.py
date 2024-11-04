from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[href*='cart?prehydrateClick=true']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6) # wait for search results page to load

    def click_cart(self):
        self.click(*self.CART_BTN)