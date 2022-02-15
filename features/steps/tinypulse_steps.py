import names
from behave import *

from utilities import constants, locators
from utilities.initial_browser import get_browser


@given("We are on the TINYpulse login page")
def impl_step(context):
    context.driver = get_browser(constants.BROWSER)
    context.driver.open(constants.LOGIN_PAGE)
    context.driver.maximize()


@when("We login by entering username & password")
def step_impl(context):
    context.driver.send_keys(locators.user_textbox, constants.USER)
    context.driver.click(locators.continue_button)
    context.driver.wait_and_send_keys(locators.passwd_textbox, constants.PASSWD)
    context.driver.click(locators.signin_button)


@then("We successfully login to system")
def step_impl(context):
    assert context.driver.is_element_visible(locators.avatar_img), True


@when("We click on {button}")
def step_impl(context, button):
    if 'settings' in button.lower():
        context.driver.wait_and_click(locators.setting_icon)
    elif 'add people' in button.lower():
        context.driver.click_by_javascript(locators.add_people_textbox)


@step("We add {condition} into list")
def step_impl(context, condition):
    number = int(condition.split(' ')[0])
    for _ in range(int(number)):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        email = "{}_{}@gmail.com".format(first_name, last_name)
        if 'first name' not in condition:
            context.driver.wait_and_send_keys(locators.first_name_textbox, first_name)
        if 'last name' not in condition:
            context.driver.wait_and_send_keys(locators.last_name_textbox, last_name)
        if 'email' not in condition:
            context.driver.send_keys(locators.email_textbox, email)
        context.driver.click(locators.start_day_textbox)
        context.driver.wait_and_click(locators.date_picker)
        context.driver.click(locators.manager_dropdown_menu)
        context.driver.wait_and_click(locators.email_item)
    context.driver.click(locators.add_people_button)


@then("We verify Congratulations page displays")
def step_impl(context):
    assert context.driver.is_element_visible(locators.congratulations_text), True
    context.driver.close()


@then("We verify an error will display")
def step_impl(context):
    assert context.driver.is_element_visible(locators.error_text), True
    context.driver.close()