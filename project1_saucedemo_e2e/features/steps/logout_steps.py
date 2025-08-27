from behave import given, when, then
from selenium.webdriver.common.by import By
from utils.selenium_helpers import parse_locator, enter_text, wait_and_click, get_text, get_attribute
from pages.pages_locators import LOGIN_PAGE, INVENTORY_PAGE


@when("I open the side menu")
def step_open_side_menu(context):
    by, loc = parse_locator(INVENTORY_PAGE["side_menu"])
    wait_and_click(context.driver, by, loc)

@when("I click the logout link")
def step_click_logout(context):
    by, loc = parse_locator(INVENTORY_PAGE["logout_button"])
    wait_and_click(context.driver, by, loc)

@then("I should be redirected back to the login page")
def step_verify_redirect_to_login(context):
    current_url = context.driver.current_url
    assert "saucedemo.com" in current_url
    assert current_url.endswith("/")

@then("I should see the login button")
def step_verify_login_button_visible(context):
    by, loc = parse_locator(LOGIN_PAGE["login_button"])
    button_text = get_attribute(context.driver, by, loc, "value")
    assert button_text.lower() == "login"