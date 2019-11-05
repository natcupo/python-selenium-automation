from behave import given, when, then
from selenium.webdriver.common.by import By

ORDERS = (By. ID, 'nav-orders')
SIGN = (By.CSS_SELECTOR, 'h1.a-spacing-small')


@given('Open Amazon')
def open_amazon_page(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_page()


@when('Click on orders button')
def click_on_orders(context):
    # context.driver.find_element(*ORDERS).click()
    context.app.main_page.click_button()


@then('Verify {expected_text} page is opened')
def sing_in_open(context, expected_text):
    # sign_in = context.driver.find_element(*SIGN).text
    # assert 'sign_in' in sign_in, f'Expected sign_in, but got {sign_in}'
    context.app.verify_result_page.verify_result_shown(expected_text)
