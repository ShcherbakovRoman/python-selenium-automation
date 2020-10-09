from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


SEARCH_INPUT = (By.ID, 'helpsearch')
SEARCH_RESULT = (By.XPATH, "//h1[text()='Cancel Items or Orders']")


# open the url
@given('Open Amazon Help page')
def open_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


# Input key words and send it
@when('Input Cancel Order into Amazon Help search field')
def input_search_words(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys('Cancel Order', Keys.ENTER)


#veriify the results
@then('First Help result contains Cancel Items or Orders')
def check_result(context):
    result = context.driver.find_element(*SEARCH_RESULT)
    assert result.text == 'Cancel Items or Orders', f'Error. Expected Cancel Items or Orders but got {result.text}'


# close the browser
def close_browser(context):
    context.driver.quit()