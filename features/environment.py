import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def before_scenario(context,driver):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_scenario(context,driver):
    context.driver.close()
    context.driver.quit()