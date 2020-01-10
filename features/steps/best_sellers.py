from behave import given, when, then
from selenium.webdriver.common.by import By

BEST_SELLERS = (By.XPATH, "//a[contains(@href,'bestsellers')]")
TOP_LINKS = (By.CSS_SELECTOR, "li.zg_selected")
HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')


@given('Open Amazon sellers page')
def open_amazon_sellers(context):
    context.driver.get('https://www.amazon.com')


@when('Click on Best Sellers')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()


@then('User can click through top links and verify page has opened')
def click_thru_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)
    for x in range(len(top_links)):
        link_to_click = context.driver.find_elements(*TOP_LINKS)[x]
        link_text = link_to_click.text
        link_to_click.click()

        new_text = context.driver.find_element(*HEADER).text
        assert link_text in new_text, f'Expected {link_text} to be in {new_text}'
