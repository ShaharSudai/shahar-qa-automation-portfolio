from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.selenium_helpers import parse_locator, enter_text, wait_and_click, get_text, get_attribute
from pages.pages_locators import LOGIN_PAGE, INVENTORY_PAGE

@when("I am on the inventory page")
def step_on_inventory_page(context):
    by, loc = parse_locator(INVENTORY_PAGE["page_title"])
    title = get_text(context.driver, by, loc)
    assert title == "Products"


@then("I should see a list of products")
def step_see_list_of_products(context):
    by, loc = parse_locator(INVENTORY_PAGE["product_list"])
    products = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by, loc))
    )
    assert len(products) > 0, "No products were found on the inventory page"

    for p in products:
        print(p.text)

@then("each product should have a name and a price")
def step_products_have_name_and_price(context):
    by_names, loc_names = parse_locator(INVENTORY_PAGE["product_names"])
    by_prices, loc_prices = parse_locator(INVENTORY_PAGE["product_prices"])

    product_names = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by_names, loc_names))
    )
    product_prices = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by_prices, loc_prices))
    )

    assert len(product_names) == len(product_prices) > 0, "Mismatch between products and prices"

    for name, price in zip(product_names, product_prices):
        assert name.text.strip() != "", "Found a product with empty name"
        assert price.text.strip().startswith("$"), f"Price invalid: {price.text}"


@when('I click on "Add to cart" for a product')
def step_add_product_to_cart(context):
    by, loc = parse_locator(INVENTORY_PAGE["first_add_to_cart_button"])
    wait_and_click(context.driver, by, loc)


@then("the cart icon should show 1 item")
def step_cart_icon_one_item(context):
    by, loc = parse_locator(INVENTORY_PAGE["cart_badge"])
    badge = get_text(context.driver, by, loc)
    assert badge == "1"


@given("I have added a product to the cart")
def step_given_product_added_to_cart(context):
    by, loc = parse_locator(INVENTORY_PAGE["first_add_to_cart_button"])
    wait_and_click(context.driver, by, loc)


@when('I click on "Remove" for that product')
def step_remove_product_from_cart(context):
    by, loc = parse_locator(INVENTORY_PAGE["first_remove_button"])
    wait_and_click(context.driver, by, loc)


@then("the cart icon should show no number")
def step_cart_icon_zero_items(context):
    by, loc = parse_locator(INVENTORY_PAGE["cart_badge"])

    WebDriverWait(context.driver, 5).until(
        EC.invisibility_of_element_located((by, loc))
    )


@when('I sort the products by "Price (low to high)"')
def step_sort_products_low_to_high(context):
    by, loc = parse_locator(INVENTORY_PAGE["sort_dropdown"])
    dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((by, loc))
    )
    Select(dropdown).select_by_value("lohi")

def _parse_price(text: str) -> float:
    return float(text.replace("$", "").strip())

@then("the first product should be the cheapest")
def step_first_product_cheapest(context):
    by, loc = parse_locator(INVENTORY_PAGE["product_prices"])
    price_els = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by, loc))
    )
    prices = [_parse_price(el.text) for el in price_els]
    assert len(prices) > 0, "No prices found"

    non_decreasing = all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1))
    assert non_decreasing, f"Prices are not ascending: {prices}"
    assert prices[0] == min(prices), f"First price {prices[0]} is not the min {min(prices)}"


@then("the last product should be the most expensive")
def step_last_product_expensive(context):
    by, loc = parse_locator(INVENTORY_PAGE["product_prices"])
    price_els = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by, loc))
    )
    prices = [_parse_price(el.text) for el in price_els]
    assert prices, "No prices found"

    assert all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1)), f"Prices not ascending: {prices}"
    assert prices[-1] == max(prices), f"Last is {prices[-1]}, max is {max(prices)}"


@when('I sort the products by "Name (A to Z)"')
def step_sort_products_name_atoz(context):
    by, loc = parse_locator(INVENTORY_PAGE["sort_dropdown"])
    dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((by, loc))
    )
    Select(dropdown).select_by_value("az")


@then('the first product should start with "A"')
def step_first_product_starts_with_a(context):
    by, loc = parse_locator(INVENTORY_PAGE["product_names"])  # "class=inventory_item_name"
    name_els = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((by, loc))
    )
    names = [el.text.strip().lower() for el in name_els]
    assert len(names) > 0, "No products found"
    assert names == sorted(names), f"Names are not A->Z: {names}"