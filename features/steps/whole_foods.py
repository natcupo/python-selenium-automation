from behave import given, when, then
from selenium.webdriver.common.by import By

WHOLE_SECTION = (By. CSS_SELECTOR, 'ul.wfm-desktop-list-font-unset li')
WORD_REGULAR = (By.XPATH, "//span[contains(text(),'Regular $9.99 ea')]")


@given("Open Amazon Whole foods page")
def open_amazon_wholefoods_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@when('Verify products contain word Regular')
def verify_product_has_word_and_name(context):
    expected_word = 'Regular'
    web_elements = context.driver.find_elements(*WORD_REGULAR)
    print(context.driver.find_element(*WORD_REGULAR).text)
    for x in range(len(web_elements)):
        web_elements[x].click()
        actual_word = context.driver.find_element(*WORD_REGULAR).text
        assert expected_word in actual_word, f'Expected, "{expected_word}", but got, "{actual_word}"'









