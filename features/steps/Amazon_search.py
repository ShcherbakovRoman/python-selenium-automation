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
    context.app.main_page.open_amazon()


@when("Input Shoes into Amazon search field")
def input_search_word(context):
    context.app.main_page.input_search_word('Shoes')


@when('Click on Amazon search icon')
def click_search(context):
    context.app.main_page.click_search_icon()


@then('First Amazon result contains Shoes')
def result_check(context):
    context.app.search_results.verify_search_result('"Shoes"')


@then('Verify Sign In is visible')
def signup_vis(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_BTN))


@when('Wait for {sec} seconds')
def sleep_sec(context, sec):
    sleep(int(sec))


@then('Verify Sign In disappears')
def signup_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_BTN))


@when('Click Amazon Orders link')
def click_orders(context):
    context.app.main_page.click_orders()

@then('Verify Sign In page is opened')
def verify_signin(context):
    context.app.singin_page.verify_signin_module('Sign-In')


@then('Verify \'Your Amazon Cart is empty\' text present')
def verify_empty_cart(context):
    context.app.cart_page.verify_cart_empty('Your Amazon Cart is empty')


@when('Click on hamburger menu')
def click_ham_menu(context):
    context.app.main_page.click_ham_menu()

@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.app.ham_menu.click_amazon_music()

@then('{qty} menu items are present')
def verify_music_items_present(context, qty):
    context.app.ham_menu.verify_links_qty(int(qty))


@when('Select Electronics department')
def select_electronics_department(context):
    context.app.main_page.select_electronics_department()


@when('Search for {Product}')
def search_for_product(context, Product):
    context.app.main_page.input_search_word(Product)
    context.app.main_page.click_search_icon()


@then('Verify electronics department is selected')
def verify_electronics_department_selected(context):
    context.app.main_page.verify_electronics_department_selected()








