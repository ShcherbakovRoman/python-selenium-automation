from pages.main_page import MainPage
from pages.product_page import Product
from pages.search_results import SearchResults
from pages.singin_page import SingInPage
from pages.cart_page import Cart
from pages.ham_menu import HamMenu

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results = SearchResults(self.driver)
        self.singin_page = SingInPage(self.driver)
        self.cart_page = Cart(self.driver)
        self.ham_menu = HamMenu(self.driver)
        self.product_page = Product(self.driver)
