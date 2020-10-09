from selenium.webdriver.common.by import By
from behave import given, when, then

FIND_CART = (By.CSS_SELECTOR, "a#nav-cart")
FIND_EMPTY = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty h2")

@given('Open Amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*FIND_CART).click()


@then('Verify Cart is empty')
def verify_empty_cart(context):
    result = context.driver.find_element(*FIND_EMPTY)
    assert result.text == "Your Amazon Cart is empty", f'Error. Expected Your Amazon Cart is empty, but got {result.text}'
# $x("//h2[text()='Your Amazon Cart is empty']") -- not working for some reason

# close the browser
def close_browser(context):
    context.driver.quit()