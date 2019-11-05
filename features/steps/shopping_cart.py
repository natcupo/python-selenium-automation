from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

EMPTY = (By.XPATH, "//h1[@class = 'sc-empty-cart-header']")
CART = (By.ID, 'nav-cart')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on shopping cart button')
def click_on_shopping_cart(context):
    # context.driver.find_element(By.ID, 'nav-cart').click()
    context.app.main_page.click_button()


@then('Verify the cart is {expected_text}')
def verify_result(context, expected_text):
    # result = context.driver.find_element(*EMPTY).text
    # assert "empty" in result, f"Expected text is empty, but got {result}"
    context.app.verify_result_page.verify_empty_word(expected_text)
