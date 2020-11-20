from pages.base_page import Page
from selenium.webdriver.common.by import By

class SingInPage(Page):
    SIGNIN_MSG = (By.CSS_SELECTOR, ".a-box-inner.a-padding-extra-large .a-spacing-small")

    def verify_signin_module(self, expected_text: str):
        self.verify_text(expected_text, *self.SIGNIN_MSG)