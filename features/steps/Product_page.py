from behave import given, when, then
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name span.selection")


@given('Open Amazon product {ProductId} page')
def open_product_page(context, ProductId):
    context.app.product_page.open_product_page(ProductId)


@then('Verify all colors are displayed')
def verify_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash', 'Light Wash', 'Medium Wash', 'Rinse', 'Vintage Light Wash']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range(len(colors)):
        colors[i].click()
        color_text = context.driver.find_element(*SELECTED_COLOR)
        assert color_text.text == expected_colors[i], f'Colors not match. Expected {expected_colors[i]} but got {color_text.text}'

@when('Hover over Add to Cart button')
def hover_addtocart_btn(context):
    context.app.product_page.hover_over()


@then('Verify if tooltip is being displayed')
def verify_tooltip(context):
    context.app.product_page.verify_tooltip()


@when('Hover over New Arrivals link')
def hover_over_newarrivals(context):
    context.app.product_page.hover_over_newarrivals()

@then('Verify if deals are displayed')
def verify_deals_displayed(context):
    context.app.product_page.verify_newarrivals_displayed()

