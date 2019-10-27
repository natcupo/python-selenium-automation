from behave import given, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

driver = webdriver.Chrome(executable_path='drivers/chromedriver')
driver.wait = WebDriverWait(driver, 5)

SEE_ALL_DEALS = (By.CSS_SELECTOR, "span.as-title-block-right")
TODAY_DEALS = (By.CSS_SELECTOR, "div.gbh1-bold")
PRODUCT = (By.ID, "101_dealView_1")
ADD_TO_CART = (By.NAME, "submit.add-to-cart")
ITEMS = (By.ID, "nav-cart-count")
ONE_ITEM = (By.ID, "sc-subtotal-label-activecart")


@given('Amazon today deal page')
def open_amazon_deal_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Open Deals')
def click_open_deals(context):
    context.driver.find_element(*SEE_ALL_DEALS).click()


@when('Switch to the new openly window')
def switch_to_new_window(context):
    driver.wait.until(EC.new_window_is_opened)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to_window(new_window)


@when('Today deals are shown')
def today_deals_shown(context):
    word = "'Today's Deals'"
    expected_words = context.driver.find_element(*TODAY_DEALS).text


@when('Click on product name')
def click_on_product(context):
    context.driver.find_element(*PRODUCT).click()


@when('Add product to cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()


@when('User can close new window and switch back to original')
def close_window_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)


@when('Refresh page')
def refreshing(context):
    driver.refresh()


@when('Click on cart')
def click_on_cart(context):
    context.driver.find_element(By.ID, "nav-cart")


@when('Cart has one item in it')
def cart_has_item(context):
    context.driver.find_element(*ITEMS).click()


@when('Verify there is one item')
def cart_has_one_item(context):
    one = 'Subtotal (1 item)'
    item = context.driver.find_element(*ONE_ITEM).text
