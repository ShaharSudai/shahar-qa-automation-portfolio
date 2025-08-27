from behave import given, when, then
from selenium.webdriver.common.by import By
from utils.selenium_helpers import parse_locator, enter_text, wait_and_click, get_text
from pages.pages_locators import LOGIN_PAGE, INVENTORY_PAGE

@given("I am logged in to the SauceDemo application")
def step_logged_in(context):
    context.driver.get("https://www.saucedemo.com/")

    by_user, loc_user = parse_locator(LOGIN_PAGE["username_field"])
    enter_text(context.driver, by_user, loc_user, "standard_user")

    by_pass, loc_pass = parse_locator(LOGIN_PAGE["password_field"])
    enter_text(context.driver, by_pass, loc_pass, "secret_sauce")

    by_btn, loc_btn = parse_locator(LOGIN_PAGE["login_button"])
    wait_and_click(context.driver, by_btn, loc_btn)
