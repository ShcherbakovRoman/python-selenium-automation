from behave import given, when, then
from selenium.webdriver.common.by import By

ITEMS = (By.CSS_SELECTOR, "#wfm-pmd_deals_section div:nth-of-type(6) li")
PRODUCT_NAME = (By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")


@given('Open Wholefoods page')
def open_wholefoods_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Each product has Product name and Regular')
def check_items(context):
    all_items = context.driver.find_elements(*ITEMS)
    for item in all_items:
        assert "Regular" in item.text, f"Expected 'Regular' to be in {item.text}"
        assert item.find_element(*PRODUCT_NAME)
