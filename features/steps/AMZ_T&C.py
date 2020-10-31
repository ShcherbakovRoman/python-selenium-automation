from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

APP_LINK = (By.XPATH, "//a[contains(text(), 'Amazon applications')]")
APP_PAGE_TEXT = (By.ID, "mgt-email-sms-download-header")

@given('Open Amazon T&C page')
def open_tc(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_windows(context):
    context.original_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon applications link')
def click_link(context):
    context.driver.find_element(*APP_LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.new_window = context.driver.window_handles
    for window in context.original_windows:
        context.new_window.remove(window)
    context.driver.switch_to_window(context.new_window[0])


@then('Amazon app page is opened')
def verify_app_page_opened(context):
    context.driver.find_element(*APP_PAGE_TEXT)


@then('User can close new window and switch back to original')
def return_to_orig_page(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
