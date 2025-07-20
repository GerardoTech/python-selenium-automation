from selenium.webdriver.common.by import By
from pages.base_page import Page


SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def verify_results_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def click_add_to_cart(self):
        self.click(*ADD_TO_CART_BTN)

    def store_product_name_from_side_nav(self):
        self.is_visible(*SIDE_NAV_PRODUCT_NAME)  # ensures it’s loaded
        return self.find_element(*SIDE_NAV_PRODUCT_NAME).text

    def confirm_add_to_cart_side_nav(self):
        self.click(*SIDE_NAV_ADD_TO_CART_BTN)