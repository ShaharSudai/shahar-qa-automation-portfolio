from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.selenium_helpers import parse_locator, enter_text, wait_and_click, get_text, get_attribute
from pages.pages_locators import LOGIN_PAGE, INVENTORY_PAGE, CART_PAGE, CHECKOUT_PAGE, CHECKOUT_OVERVIEW_PAGE


@when("I continue without filling the first name")
def step_continue_without_first_name(context):
    by_last, loc_last = parse_locator(CHECKOUT_PAGE["last_name_field"])
    enter_text(context.driver, by_last, loc_last, "Sudai")

    by_postal, loc_postal = parse_locator(CHECKOUT_PAGE["postal_code_field"])
    enter_text(context.driver, by_postal, loc_postal, "12345")

    by_continue, loc_continue = parse_locator(CHECKOUT_PAGE["continue_button"])
    wait_and_click(context.driver, by_continue, loc_continue)

@then("I should see an error message that first name is required")
def step_error_first_name_required(context):
    by, loc = parse_locator(CHECKOUT_PAGE["error_message"])
    error_text = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((by, loc))
    ).text.strip()

    assert error_text == "Error: First Name is required", \
        f'Unexpected error message: "{error_text}"'

@when("I continue without filling the last name")
def step_continue_without_last_name(context):
    by_first, loc_first = parse_locator(CHECKOUT_PAGE["first_name_field"])
    enter_text(context.driver, by_first, loc_first, "Shahar")

    by_postal, loc_postal = parse_locator(CHECKOUT_PAGE["postal_code_field"])
    enter_text(context.driver, by_postal, loc_postal, "12345")

    by_continue, loc_continue = parse_locator(CHECKOUT_PAGE["continue_button"])
    wait_and_click(context.driver, by_continue, loc_continue)

@then("I should see an error message that last name is required")
def step_error_last_name_required(context):
    by, loc = parse_locator(CHECKOUT_PAGE["error_message"])
    error_text = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((by, loc))
    ).text.strip()

    assert error_text == "Error: Last Name is required", \
        f'Unexpected error message: "{error_text}"'

@when("I continue without filling the postal code")
def step_continue_without_postal_code(context):
    by_first, loc_first = parse_locator(CHECKOUT_PAGE["first_name_field"])
    enter_text(context.driver, by_first, loc_first, "Shahar")

    by_last, loc_last = parse_locator(CHECKOUT_PAGE["last_name_field"])
    enter_text(context.driver, by_last, loc_last, "Sudai")

    by_continue, loc_continue = parse_locator(CHECKOUT_PAGE["continue_button"])
    wait_and_click(context.driver, by_continue, loc_continue)

@then("I should see an error message that postal code is required")
def step_error_postal_code_required(context):
    by, loc = parse_locator(CHECKOUT_PAGE["error_message"])
    error_text = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((by, loc))
    ).text.strip()

    assert error_text == "Error: Postal Code is required", \
        f'Unexpected error message: "{error_text}"'

@when('I click "Cancel" on checkout step one')
def step_cancel_checkout_step_one(context):
    by, loc = parse_locator(CHECKOUT_PAGE["cancel_button"])
    wait_and_click(context.driver, by, loc)

@when("I fill valid checkout information")
def step_fill_valid_checkout_information(context):
    by_first, loc_first = parse_locator(CHECKOUT_PAGE["first_name_field"])
    enter_text(context.driver, by_first, loc_first, "Shahar")

    by_last, loc_last = parse_locator(CHECKOUT_PAGE["last_name_field"])
    enter_text(context.driver, by_last, loc_last, "Sudai")

    by_postal, loc_postal = parse_locator(CHECKOUT_PAGE["postal_code_field"])
    enter_text(context.driver, by_postal, loc_postal, "12345")

@when('I click "Continue"')
def step_click_continue(context):
    by_continue, loc_continue = parse_locator(CHECKOUT_PAGE["continue_button"])
    wait_and_click(context.driver, by_continue, loc_continue)

# Step Two (Overview)
@then("I should see the selected items in the overview")
def step_overview_shows_selected_items(context):
    pass

@then("the item total should equal the sum of item prices")
def step_item_total_equals_sum(context):
    pass

@then("I should see a tax amount")
def step_overview_shows_tax(context):
    pass

@then("the total should equal item total plus tax")
def step_total_equals_item_total_plus_tax(context):
    pass

@when('I click "Cancel" on checkout step two')
def step_cancel_checkout_step_two(context):
    pass


@when('I click "Finish"')
def step_click_finish(context):
    pass

@then("I should be redirected to the checkout complete page")
def step_redirected_to_checkout_complete(context):
    pass

@then("I should see a confirmation message for the order")
def step_see_order_confirmation_message(context):
    pass

@when('I click "Back Home"')
def step_click_back_home(context):
    pass
