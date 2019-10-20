from behave import given, when, then
from selenium.webdriver.common.by import By

COLOR_OPTION = (By.CSS_SELECTOR, "div#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "div#variation_color_name span.selection")

@given('Amazon Jeans B07BKD8JCQ')
def open_amazon_jeans_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BKD8JCQ/')


@when('Verify user can select through colors')
def verify_colors(context):
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']
    color_web_elements = context.driver.find_elements(*COLOR_OPTION)
    for x in range(len(color_web_elements)):
        color_web_elements[x].click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        print(actual_color)
        assert actual_color == expected_colors[x], f'Expected {expected_colors[x]}, but got (actual color)'




