from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon Internet page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when ('Click on Try Prime')
def click_try_prime(context):
    context.driver.find_element(By. XPATH, "//span[text()='Try Prime']").click()


@when('Click on try button')
def click_try_button(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.prime-button-try').click()


@then('Verify 8 boxes are present')
def verify_items(context):
    print(len(context.driver.find_elements(By.CSS_SELECTOR, 'div.a-padding-base')))
    value = len(context.driver.find_elements(By.CSS_SELECTOR, 'div.a-padding-base'))
    assert value == 4, f'Expected 8 items, but got value'






