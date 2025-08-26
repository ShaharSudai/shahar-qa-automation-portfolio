from behave import given, when, then
from selenium.webdriver.common.by import By
from utils.selenium_helpers import parse_locator, enter_text, wait_and_click, get_text
from pages.pages_locators import LOGIN_PAGE, INVENTORY_PAGE

# Background
@given("I am on the SauceDemo login page")
def step_given_on_login_page(context):
    context.driver.get("https://www.saucedemo.com/")

# Scenario: Successful login with valid credentials
@when("I enter a valid username")
def step_when_enter_valid_username(context):
    by, loc = parse_locator(LOGIN_PAGE["username_field"])
    enter_text(context.driver, by, loc, "standard_user")

@when("I enter a valid password")
def step_when_enter_valid_password(context):
    by, loc = parse_locator(LOGIN_PAGE["password_field"])
    enter_text(context.driver, by, loc, "secret_sauce")

@when("I click the login button")
def step_when_click_login_button(context):
    by, loc = parse_locator(LOGIN_PAGE["login_button"])
    wait_and_click(context.driver, by, loc)

@then("I should be redirected to the inventory page")
def step_then_redirected_to_inventory(context):
    by, loc = parse_locator(INVENTORY_PAGE["page_title"])
    title = get_text(context.driver, by, loc)
    assert title == "Products"

@then("I should see the products list")
def step_then_see_products_list(context):
    by, loc = parse_locator(INVENTORY_PAGE["product_list"])
    product_name = get_text(context.driver, by, loc)
    assert product_name != ""


# Scenario: Login with invalid password
@when("I enter an invalid password")
def step_when_enter_invalid_password(context):
    by, loc = parse_locator(LOGIN_PAGE["password_field"])
    enter_text(context.driver, by, loc, "wrong_password")

@then("I should see an error message indicating invalid credentials")
def step_then_error_invalid_credentials(context):
    by, loc = parse_locator(LOGIN_PAGE["error_message"])
    error_text = get_text(context.driver, by, loc)
    assert "Epic sadface" in error_text or "not match" in error_text


# Scenario: Login with locked out user
@when("I enter a locked out username")
def step_when_enter_locked_out_username(context):
    by, loc = parse_locator(LOGIN_PAGE["username_field"])
    enter_text(context.driver, by, loc, "locked_out_user")

@then("I should see an error message that the user is locked out")
def step_then_error_user_locked_out(context):
    by, loc = parse_locator(LOGIN_PAGE["error_message"])
    error_text = get_text(context.driver, by, loc)
    assert "locked out" in error_text.lower()


# Scenario: Login with empty username and password
@when("I click the login button without entering credentials")
def step_when_click_login_without_credentials(context):
    by, loc = parse_locator(LOGIN_PAGE["login_button"])
    wait_and_click(context.driver, by, loc)

@then("I should see an error message that username is required")
def step_then_error_username_required(context):
    by, loc = parse_locator(LOGIN_PAGE["error_message"])
    error_text = get_text(context.driver, by, loc)
    assert "Username is required" in error_text


# Scenario: Login with empty password
@when("I leave the password field empty")
def step_when_leave_password_empty(context):
    pass

@then("I should see an error message that password is required")
def step_then_error_password_required(context):
    by, loc = parse_locator(LOGIN_PAGE["error_message"])
    error_text = get_text(context.driver, by, loc)
    assert "Password is required" in error_text
