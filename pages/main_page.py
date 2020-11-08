from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    ICON_CLICK = (By.XPATH, "//input[@value='Go']")
    ORDERS_LINK = (By.CSS_SELECTOR, '#nav-orders')
    CART_ICON = (By.CSS_SELECTOR, "a#nav-cart")
    HAM_MENU = (By.CSS_SELECTOR, "#nav-hamburger-menu")
    AMZ_MUSIC = (By.XPATH, "//div[contains(text(), 'Amazon Music')]")

    def open_amazon(self):
        self.open_page('https://www.amazon.com')

    def input_search_word(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)

    def click_search_icon(self):
        self.click(*self.ICON_CLICK)

    def click_orders(self):
        self.click(*self.ORDERS_LINK)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_ham_menu(self):
        self.click(*self.HAM_MENU)

    def click_amazon_music(self):
        self.click(*self.AMZ_MUSIC)



