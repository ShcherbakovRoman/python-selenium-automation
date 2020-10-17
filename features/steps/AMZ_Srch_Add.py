from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
PRICE_CLICK = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
ADD_TO_CART = (By.CSS_SELECTOR, "input#add-to-cart-button")
FIND_CART = (By.CSS_SELECTOR, "a#nav-cart")


@given('Open new Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when("Input Flashlight into Amazon search field and search for it")
def input_search_word(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys('Flashlight', Keys.ENTER)


@when("Add any product to Cart")
def add_to_cart(context):
    context.driver.find_element(*PRICE_CLICK).click()
    context.driver.find_element(*ADD_TO_CART).click()


@then("Confirm this product is added to Cart")
def confirm_product(context):
    context.driver.find_element(*FIND_CART).click()
    result = context.driver.find_element(By.XPATH, "//span[@id='sc-subtotal-label-activecart']")
    assert result.text == 'Subtotal (1 item):', f'No items in Cart'



