import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import allure

# def before_scenario(context,driver):
#     context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     context.driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
#     context.driver.implicitly_wait(10)
#
#
# def after_scenario(context,driver):
#     context.driver.close()
#     context.driver.quit()


@given(u'user is on login page')
def step_impl(context):
    print("user is on login page")
    # context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # context.driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    # context.driver.implicitly_wait(10)
    # context.driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    context.driver.find_element(By.XPATH,"//*[contains(@href,'account/account')][@title='My Account']").click()
    context.driver.find_element(By.LINK_TEXT,"Login").click()



@when(u'user enters "{username}" and "{password}"')
def step_impl(context,username,password):
    # enter_username = context.driver.find_element(By.NAME,"username")
    # enter_password = context.driver.find_element(By.NAME,"password")
    # enter_password.send_keys("Admin")
    # enter_password.send_keys("admin123")

    enter_username = context.driver.find_element(By.NAME, "email")
    enter_password = context.driver.find_element(By.NAME, "password")
    enter_username.send_keys(username)
    enter_password.send_keys(password)



@when(u'click login button')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH,"//*[@class='btn btn-primary' and @value='Login']")
    login_button.click()



@then(u'On Success full login"{text}" is displayed on home page')
def step_impl(context,text):
    home_page = context.driver.find_element(By.XPATH, "//h1/a").text
    assert text == home_page, f"the displayed text is not matching with expected {text}"
    allure.attach(context.driver.get_screenshot_as_png(),
    name="Login Screenshot",attachment_type=allure.attachment_type.PNG )
    allure.attach(
        "Login successful",
        name="Execution Log",
        attachment_type=allure.attachment_type.TEXT
    )
    # context.driver.close()
    # context.driver.quit()
    time.sleep(1)