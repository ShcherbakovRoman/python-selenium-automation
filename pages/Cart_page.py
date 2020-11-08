from pages.base_page import Page
from selenium.webdriver.common.by import By

class Cart(Page):
    FIND_EMPTY = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty h2")

    def verify_cart_empty(self, expected_text):
        self.verify_text(expected_text, *self.FIND_EMPTY)