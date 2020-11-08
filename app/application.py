from pages.main_page import MainPage
from pages.search_results import SearchResults
from pages.SingIn_page import SingInPage
from pages.Cart_page import Cart

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results = SearchResults(self.driver)
        self.SingIn_page = SingInPage(self.driver)
        self.Cart_page = Cart(self.driver)
