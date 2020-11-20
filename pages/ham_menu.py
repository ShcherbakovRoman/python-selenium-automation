from pages.base_page import Page
from selenium.webdriver.common.by import By

class HamMenu(Page):
    AMZ_MUSIC_MENU = (By.CSS_SELECTOR, "ul.hmenu-translateX a[class=hmenu-item]")
    AMZ_MUSIC = (By.XPATH, "//div[contains(text(), 'Amazon Music')]")

    def click_amazon_music(self):
        self.click(*self.AMZ_MUSIC)

    def verify_links_qty(self, qty):
        self.driver.wait.until(
            lambda driver: len(driver.find_elements(*self.AMZ_MUSIC_MENU)) == qty,
            f'Amount of items did not match. Expected {qty}'
        )
