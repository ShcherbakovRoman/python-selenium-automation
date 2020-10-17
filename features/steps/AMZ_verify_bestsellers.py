from behave import given, when, then
from selenium.webdriver.common.by import By


LINKS = (By.XPATH, "//a[contains(@href, 'ref=zg_bs_tab')]")

@given('Open BestSellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Find 5 links')
def find_link_count(context):
    links = len(context.driver.find_elements(*LINKS))
    assert links == 5, f'Error. Expected 5, but got {links}'