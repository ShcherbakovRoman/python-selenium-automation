from behave import given, when, then
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name span.selection")


@given('Open Amazon product {ProductId} page')
def open_product_page(context, ProductId):
    context.driver.get(f'https://www.amazon.com/gp/product/{ProductId}')


@then('Verify all colors are displayed')
def verify_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash', 'Light Wash', 'Medium Wash', 'Rinse', 'Vintage Light Wash']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range(len(colors)):
        colors[i].click()
        color_text = context.driver.find_element(*SELECTED_COLOR)
        assert color_text.text == expected_colors[i], f'Colors not match. Expected {expected_colors[i]} but got {color_text.text}'

