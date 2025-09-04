from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.selenium_helpers import parse_locator, enter_text, wait_and_click, get_text, get_attribute
from pages.pages_locators import LOGIN_PAGE, INVENTORY_PAGE, CART_PAGE, CHECKOUT_PAGE, CHECKOUT_OVERVIEW_PAGE, CHECKOUT_COMPLETE_PAGE


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
    by, loc = parse_locator(CHECKOUT_OVERVIEW_PAGE["overview_item_names"])
    name_els = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by, loc))
    )
    names = [el.text.strip() for el in name_els]
    assert names, "No items found in checkout overview"

    if hasattr(context, "selected_product_name"):
        assert context.selected_product_name in names, \
            f'Expected "{context.selected_product_name}" in overview, got {names}'
    elif hasattr(context, "selected_products"):
        for p in context.selected_products:
            assert p in names, f'Expected "{p}" in overview, got {names}'

def _parse_price(text: str) -> float:
    return float(text.replace("Item total: $", "").replace("$", "").strip())

@then("the item total should equal the sum of item prices")
def step_item_total_equals_sum(context):
    by_prices, loc_prices = parse_locator(CHECKOUT_OVERVIEW_PAGE["overview_item_prices"])
    price_els = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by_prices, loc_prices))
    )
    prices = [float(el.text.replace("$", "").strip()) for el in price_els]


    by_total, loc_total = parse_locator(CHECKOUT_OVERVIEW_PAGE["item_total_label"])
    total_text = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((by_total, loc_total))
    ).text.strip()

    displayed_total = _parse_price(total_text)
    calculated_total = sum(prices)

    assert abs(displayed_total - calculated_total) < 0.01, \
        f"Displayed total {displayed_total} != sum of prices {calculated_total}"

@then("I should see a tax amount")
def step_overview_shows_tax(context):
    by, loc = parse_locator(CHECKOUT_OVERVIEW_PAGE["tax_label"])
    tax_text = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((by, loc))
    ).text.strip()

    assert tax_text.startswith("Tax:"), f"Unexpected tax label: {tax_text}"

    try:
        tax_value = float(tax_text.replace("Tax: $", "").strip())
    except ValueError:
        raise AssertionError(f"Tax amount is not a valid number: {tax_text}")

    assert tax_value >= 0, f"Tax value should be non-negative, got {tax_value}"

@then("the total should equal item total plus tax")
def step_total_equals_item_total_plus_tax(context):
    by_item_total, loc_item_total = parse_locator(CHECKOUT_OVERVIEW_PAGE["item_total_label"])
    by_tax, loc_tax = parse_locator(CHECKOUT_OVERVIEW_PAGE["tax_label"])
    by_total, loc_total = parse_locator(CHECKOUT_OVERVIEW_PAGE["total_label"])

    item_total_text = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((by_item_total, loc_item_total))
    ).text.strip()  # "Item total: $39.98"

    tax_text = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((by_tax, loc_tax))
    ).text.strip()  # "Tax: $3.20"

    total_text = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((by_total, loc_total))
    ).text.strip()  # "Total: $43.18"

    def _to_float(s: str) -> float:
        return float(s.replace("Item total:", "").replace("Tax:", "").replace("Total:", "").replace("$", "").strip())

    item_total = _to_float(item_total_text)
    tax = _to_float(tax_text)
    displayed_total = _to_float(total_text)
    calculated_total = item_total + tax

    assert abs(displayed_total - calculated_total) < 0.01, \
        f"Displayed total {displayed_total} != item total + tax {calculated_total} (item={item_total}, tax={tax})"


@when('I click "Cancel" on checkout step two')
def step_cancel_checkout_step_two(context):
    by, loc = parse_locator(CHECKOUT_OVERVIEW_PAGE["cancel_button_step_two"])
    wait_and_click(context.driver, by, loc)


@when('I click "Finish"')
def step_click_finish(context):
    by, loc = parse_locator(CHECKOUT_OVERVIEW_PAGE["finish_button"])
    wait_and_click(context.driver, by, loc)

# Complete
@then("I should see a confirmation message for the order")
def step_see_order_confirmation_message(context):

    by_hdr, loc_hdr = parse_locator(CHECKOUT_COMPLETE_PAGE["confirmation_header"])
    header_text = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((by_hdr, loc_hdr))
    ).text.strip()

    assert "thank you for your order" in header_text.lower(), \
        f'Unexpected confirmation header: "{header_text}"'


    by_txt, loc_txt = parse_locator(CHECKOUT_COMPLETE_PAGE["confirmation_text"])
    _ = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((by_txt, loc_txt))
    )


@when('I click "Back Home"')
def step_click_back_home(context):
    by, loc = parse_locator(CHECKOUT_OVERVIEW_PAGE["back_home_button"])
    wait_and_click(context.driver, by, loc)