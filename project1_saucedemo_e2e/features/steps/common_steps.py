from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.selenium_helpers import parse_locator, enter_text, wait_and_click, get_text, get_attribute
from pages.pages_locators import LOGIN_PAGE, INVENTORY_PAGE, CART_PAGE, CHECKOUT_PAGE

@given("I am logged in to the SauceDemo application")
def step_logged_in(context):
    context.driver.get("https://www.saucedemo.com/")

    by_user, loc_user = parse_locator(LOGIN_PAGE["username_field"])
    enter_text(context.driver, by_user, loc_user, "standard_user")

    by_pass, loc_pass = parse_locator(LOGIN_PAGE["password_field"])
    enter_text(context.driver, by_pass, loc_pass, "secret_sauce")

    by_btn, loc_btn = parse_locator(LOGIN_PAGE["login_button"])
    wait_and_click(context.driver, by_btn, loc_btn)

@given("I have added a product to the cart")
def step_given_added_one_product(context):
    context.driver.get("https://www.saucedemo.com/inventory.html")
    by_add, loc_add = parse_locator(INVENTORY_PAGE["first_add_to_cart_button"])
    wait_and_click(context.driver, by_add, loc_add)


@given("I have added 2 products to the cart")
def step_given_added_two_products(context):
    context.driver.get("https://www.saucedemo.com/inventory.html")
    by1, loc1 = parse_locator(INVENTORY_PAGE["first_add_to_cart_button"])
    by2, loc2 = parse_locator(INVENTORY_PAGE["second_add_to_cart_button"])
    wait_and_click(context.driver, by1, loc1)
    wait_and_click(context.driver, by2, loc2)

@then("I should be redirected to the inventory page")
def step_redirected_to_inventory_page(context):

    assert "/inventory.html" in context.driver.current_url, \
        f"Unexpected URL: {context.driver.current_url}"

    by, loc = parse_locator(INVENTORY_PAGE["page_title"])
    title = get_text(context.driver, by, loc)
    assert title == "Products"