from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip span")


@then("Sign In pop up is present and clickable")
def check_popup(context):
    context.driver.wait.until(EC.presence_of_element_located(SIGNIN_BTN))
    context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_BTN))


@when("Sign In pop up disappears")
def pop_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element(SIGNIN_BTN))


@then("Verify Sign In is not clickable")
def popup_not_clickable(context):
    context.driver.wait.until_not(EC.element_to_be_clickable(SIGNIN_BTN))