from behave import given, when, then
from utils.selenium_helpers import init_driver, quit_driver, enter_text, wait_and_click, get_text

# Background
@given("I am on the SauceDemo login page")
def step_given_on_login_page(context):
    pass


# Scenario: Successful login with valid credentials
@when("I enter a valid username")
def step_when_enter_valid_username(context):
    pass

@when("I enter a valid password")
def step_when_enter_valid_password(context):
    pass

@when("I click the login button")
def step_when_click_login_button(context):
    pass

@then("I should be redirected to the inventory page")
def step_then_redirected_to_inventory(context):
    pass

@then("I should see the products list")
def step_then_see_products_list(context):
    pass


# Scenario: Login with invalid password
@when("I enter an invalid password")
def step_when_enter_invalid_password(context):
    pass

@then("I should see an error message indicating invalid credentials")
def step_then_error_invalid_credentials(context):
    pass


# Scenario: Login with locked out user
@when("I enter a locked out username")
def step_when_enter_locked_out_username(context):
    pass

@then("I should see an error message that the user is locked out")
def step_then_error_user_locked_out(context):
    pass


# Scenario: Login with empty username and password
@when("I click the login button without entering credentials")
def step_when_click_login_without_credentials(context):
    pass

@then("I should see an error message that username is required")
def step_then_error_username_required(context):
    pass


# Scenario: Login with empty password
@when("I leave the password field empty")
def step_when_leave_password_empty(context):
    pass

@then("I should see an error message that password is required")
def step_then_error_password_required(context):
    pass
