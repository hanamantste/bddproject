import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@when(u'user enter "{product}" to search product')
def step_impl(context,product):
    wait = WebDriverWait(context.driver,20)
    search_button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@name='search']")))
    search_button.send_keys(product)
    # context.driver.find_element(By.NAME,"//*[@name='search']").send_keys("HP")

@when(u'click on search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[@class='input-group-btn']").click()


@then(u'respective product should be displayed "{message}"')
def step_impl(context,message):
    # assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    txt = context.driver.find_element(By.XPATH,"(//input[@id='button-search']/following::p)[last()-1]").text.strip()
    print(txt)
    assert txt.__eq__(message)


@when(u'user enter product to search product')
def step_impl(context):
    # context.driver.find_element(By.XPATH,"//*[@name='search']")
    context.driver.find_element(By.XPATH,"//*[@name='search']").send_keys("HP")


@then(u'respective product should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()