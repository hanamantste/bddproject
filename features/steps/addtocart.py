import time
from behave import *
from selenium.webdriver.common.by import By

from features.pages.Shopping import Shopping


@when(u'respective product should be displayed')
def step_impl(context):
    time.sleep(10)


@when(u'user clicks add to cart')
def step_impl(context):
    shopping_page = Shopping(context.driver)
    shopping_page.add_cart_button()


@when(u'user checkout')
def step_impl(context):
    shopping_page = Shopping(context.driver)
    shopping_page.click_cart()


@then(u'billing page should be displayed')
def step_impl(context):
    shopping_page = Shopping(context.driver)
    shopping_page.check_out_cart()
    txt = context.driver.find_element(By.CSS_SELECTOR,"[href='#collapse-checkout-option']").text.strip()
    print(f"TEXT IS DISPLAYED : -  {txt}")
    assert txt.__eq__("Step 1: Checkout Options")
    time.sleep(5)

