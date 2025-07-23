from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetAppPage(Page):
    PP_LINK = (By.XPATH, "//a[text()='Privacy policy']")
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")

    def open_target_app(self):
        self.open_url('https://www.target.com/c/target-app/')

    def click_pp_link(self):
        self.click(*self.PP_LINK)

    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_pp_opened(self):
        self.verify_partial_url('target-privacy-policy')

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions')