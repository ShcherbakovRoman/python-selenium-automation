from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

WEBSITE_LINK = (By.XPATH, "//a[contains(text(), '5flavorcafe')]")
COMPANY_NAME = (By.XPATH, "//*[contains(text(), '5 Flavor')]")

@given('Open Yelp page')
def open_yelp_page(context):
    context.driver.get('https://www.yelp.com/biz/5-flavor-cafe-portland-3')

@when('Click on a web-site link')
def click_link(context):
    context.original_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle
    link = context.driver.find_element(*WEBSITE_LINK)
    link.click()
    print(context.original_windows)
    print(context.original_window)


@when('Switch to a new window')
def switch_windows(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.new_windows = context.driver.window_handles
    print(context.new_windows)
    for window in context.original_windows:
        context.new_windows.remove(window)
    print(context.new_windows)
    context.driver.switch_to_window(context.new_windows[0])


@then('The Restaurnat\'s website is opened')
def verify_website_opened(context):
    context.driver.find_element(*COMPANY_NAME)


@then('User can close new window and return to original window')
def go_back(context):
    context.driver.close()
    # context.new_windows[0].close()
    context.driver.switch_to_window(context.original_window)