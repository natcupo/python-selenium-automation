from behave import given, when, then
from selenium.webdriver.common.by import By

HAM_MENU = (By.ID, 'nav-hamburger-menu')


@given('Open my Amazon page')
def open_amazon_deal_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on hamburger menu')
def click_ham_menu(context):
    context.app.main_page.click_menu()


@when('Click on Amazon Music Menu item')
def click_amazon_music(context):
    context.app.side_menu.click_amazon_music()


@then('{expected_item_count} menu items are present')
def verify_amount_items(context, expected_item_count):
    expected_item_count = int(expected_item_count)
    context.app.side_menu.verify_amount_items(expected_item_count)
