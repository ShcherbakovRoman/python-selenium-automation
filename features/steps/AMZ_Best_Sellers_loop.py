from behave import when, then
from selenium.webdriver.common.by import By

BEST_SELLERS = (By.CSS_SELECTOR, "#nav-xshop a:nth-of-type(3)")
TABS = (By.CSS_SELECTOR, "#zg_tabs li")
HEADER_TEXT = (By.ID, "zg_banner_text_wrapper")


@when('Click Best Sellers')
def click_bestsellers(context):
    context.driver.find_element(*BEST_SELLERS).click()


@then('Click on each top link and verify that new page opens')
def click_thru_tabs(context):
    expected_tabs = ["Best Sellers", "New Releases", "Movers & Shakers", "Most Wished For", "Gift Ideas"]
    tabs = context.driver.find_elements(*TABS)
    for i in range(len(tabs)):
        tabs = context.driver.find_elements(*TABS) # might not be the best solutioin, but it worked :)
        tabs[i].click()
        tab_header = context.driver.find_element(*HEADER_TEXT)
        assert expected_tabs[i] in tab_header.text, f"There is no {expected_tabs[i]} in {tab_header.text}"
