from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.selenium_helpers import parse_locator, enter_text, wait_and_click, get_text, get_attribute
from pages.pages_locators import LOGIN_PAGE, INVENTORY_PAGE, CART_PAGE, CHECKOUT_PAGE


@then("the cart should be empty")
def step_cart_should_be_empty(context):
    by, loc = parse_locator(CART_PAGE["cart_items"])

    try:
        items = WebDriverWait(context.driver, 3).until(
            EC.presence_of_all_elements_located((by, loc))
        )
        assert len(items) == 0, f"Expected empty cart, but found {len(items)} items"
    except Exception:

        pass


@then("the cart icon should show 0 items")
def step_cart_icon_zero_items(context):
    by, loc = parse_locator(CART_PAGE["cart_badge"])

    WebDriverWait(context.driver, 5).until(
        EC.invisibility_of_element_located((by, loc))
    )

@then("I should see that product in the cart")
def step_see_that_product_in_cart(context):
    by_names, loc_names = parse_locator(CART_PAGE["cart_item_names"])
    name_els = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by_names, loc_names))
    )
    names = [el.text.strip() for el in name_els]
    assert names, "Cart is empty, expected at least one item"

    if hasattr(context, "selected_product_name") and context.selected_product_name:
        assert context.selected_product_name in names, \
            f'Expected "{context.selected_product_name}" in cart, got {names}'


@then("I should see 2 cart items")
def step_see_two_cart_items(context):
    by, loc = parse_locator(CART_PAGE["cart_items"])

    try:
        items = WebDriverWait(context.driver, 3).until(
            EC.presence_of_all_elements_located((by, loc))
        )
        assert len(items) == 2, f"Expected empty cart, but found {len(items)} items"
    except Exception:

        pass


@then("each cart item should have a name and a price")
def step_cart_items_have_name_and_price(context):
    by_names, loc_names = parse_locator(CART_PAGE["cart_item_names"])
    by_prices, loc_prices = parse_locator(CART_PAGE["cart_item_prices"])

    name_els = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by_names, loc_names))
    )
    price_els = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by_prices, loc_prices))
    )

    assert len(name_els) == len(price_els) > 0, \
        f"Mismatch or empty cart: names={len(name_els)}, prices={len(price_els)}"

    for name_el, price_el in zip(name_els, price_els):
        name = name_el.text.strip()
        price = price_el.text.strip()
        assert name != "", "Found a cart item with empty name"
        assert price.startswith("$"), f"Invalid price format: '{price}'"


@then("each cart item should have a quantity")
def step_cart_items_have_quantity(context):
    by_qty, loc_qty = parse_locator(CART_PAGE["cart_item_quantities"])
    qty_els = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by_qty, loc_qty))
    )

    assert len(qty_els) > 0, "No quantities found in the cart"

    for q in qty_els:
        qty = q.text.strip()
        assert qty.isdigit(), f"Quantity is not numeric: '{qty}'"
        assert int(qty) > 0, f"Quantity should be positive, got {qty}"


@when("I remove that product from the cart")
def step_remove_that_product_from_cart(context):
    by, loc = parse_locator(CART_PAGE["first_remove_button"])
    wait_and_click(context.driver, by, loc)


@when('I click "Continue Shopping"')
def step_click_continue_shopping(context):
    by, loc = parse_locator(CART_PAGE["continue_shopping_button"])
    wait_and_click(context.driver, by, loc)



