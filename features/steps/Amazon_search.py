from behave import given, when, then
from selenium.webdriver.common.by import By


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
ICON_CLICK = (By.XPATH, "//input[@value='Go']")
SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when("Input Shoes into Amazon search field")
def input_search_word(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys('Shoes')


@when('Click on Amazon search icon')
def click_search(context):
    search_icon = context.driver.find_element(*ICON_CLICK)
    search_icon.click()


@then('First Amazon result contains Shoes')
def result_check(context):
    result = context.driver.find_element(*SEARCH_RESULT)
    assert result.text == '"Shoes"', f'Error. Expected Shoes but got {result.text}'
