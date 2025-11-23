import os
import time
import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def before_scenario(context,scenario):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)



def after_scenario(context,scenario):
    # if os.path.exists(context.log_file):
    #     with open(context.log_file, "r") as f:
    #         allure.attach(f.read(), name="Execution Logs", attachment_type=allure.attachment_type.TEXT)
    context.driver.quit()
