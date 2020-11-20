from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page


class Product(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    TOOLTIP_POPUP = (By.ID, 'a-popover-content-1')
    NEW_ARRIVALS_LINK = (By.XPATH, "//span[contains(text(), 'New Arrivals')]")
    NEW_ARRIVALS_DEALS = (By.ID, 'nav-flyout-aj:https://images-na.ssl-images-amazon.com/images/G/01/softlines/megamenu/prod/megamenu-contents_en_US._TTH_.json:subnav-sl-megamenu-8:0')



    def open_product_page(self, productid):
        self.open_page(f'https://www.amazon.com/gp/product/{productid}')


    def hover_over(self):
        cart_btn = self.find_elelment(*self.ADD_TO_CART_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(cart_btn).perform()


    def verify_tooltip(self):
        self.wait_for_element_appear(*self.TOOLTIP_POPUP)


    def hover_over_newarrivals(self):
        newarrivals_btn = self.find_elelment(*self.NEW_ARRIVALS_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(newarrivals_btn).perform()


    def verify_newarrivals_displayed(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DEALS)