from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
ICON_CLICK = (By.XPATH, "//input[@value='Go']")
SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
SIGN_BTN = (By.CSS_SELECTOR, "div#nav-signin-tooltip > a")

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


@then('Verify Sign In is visible')
def signup_vis(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_BTN))


@when('Wait for {sec} seconds')
def sleep_sec(context, sec):
    sleep(int(sec))


@then('Verify Sign In disappears')
def signup_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_BTN))
