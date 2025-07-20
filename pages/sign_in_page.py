from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_FORM = (By.ID, "login")

    def verify_sign_in_form_displayed(self):
        return self.is_visible(self.SIGN_IN_FORM)