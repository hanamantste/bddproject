from behave import *

from features.pages.LoginPage import LoginPage


@when(u'click on login')
def step_impl(context):
    context.login_page_1 = LoginPage(context.driver)
    login_page_1.login_to_the_application_with_valid_credentials("ragh.gr89@gmail.com",'8147151204')


@when(u'user enters username and password')
def step_impl(context):
    context.login_page_1.login_to_the_application_with_valid_credentials("ragh.gr89@gmail.com", '8147151204')



@when(u'search not in stock product')
def step_impl(context):
   pass


@then(u'should display out of stock product marked are not available')
def step_impl(context):
    pass