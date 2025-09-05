from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from utils.selenium_helpers import parse_locator, enter_text, wait_and_click, get_text, get_attribute, click_and_switch_to_new_tab, close_tab_and_switch_back
from pages.pages_locators import LOGIN_PAGE, INVENTORY_PAGE, CART_PAGE, CHECKOUT_PAGE, CHECKOUT_OVERVIEW_PAGE, CHECKOUT_COMPLETE_PAGE, PRODUCT_PAGE, FOOTER_LINKS


@when("I click the cart icon")
def step_click_cart_icon(context):
    by, loc = parse_locator(INVENTORY_PAGE["cart_page_button"])
    wait_and_click(context.driver, by, loc)

@when("I open the first product details")
def step_open_first_product_details(context):

    by_link, loc_link = parse_locator(INVENTORY_PAGE["first_product_link"])
    try:
        link_el = WebDriverWait(context.driver, 8).until(
            EC.visibility_of_element_located((by_link, loc_link))
        )
        context.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", link_el)
        WebDriverWait(context.driver, 5).until(EC.element_to_be_clickable((by_link, loc_link)))
        link_el.click()
        return
    except Exception:
        pass

@then("I should see the product details page")
def step_see_product_details_page(context):
    assert "/inventory-item.html" in context.driver.current_url, \
        f"Unexpected URL: {context.driver.current_url}"

    by_name, loc_name = parse_locator(PRODUCT_PAGE["product_name"])
    product_name = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((by_name, loc_name))
    ).text.strip()
    assert product_name != "", "Product name not visible on product details page"

@when("I click the back to products button")
def step_click_back_to_products(context):
    by, loc = parse_locator(PRODUCT_PAGE["back_button"])
    wait_and_click(context.driver, by, loc)

@when('I click "All Items"')
def step_click_all_items(context):
    by, loc = parse_locator(INVENTORY_PAGE["all_items_button"])
    wait_and_click(context.driver, by, loc)

@when('I click "Reset App State"')
def step_click_reset_app_state(context):
    by, loc = parse_locator(INVENTORY_PAGE["reset_app_state_button"])
    wait_and_click(context.driver, by, loc)

@then("the inventory should be in default state")
def step_inventory_default_state(context):
    by_badge, loc_badge = parse_locator(INVENTORY_PAGE["cart_badge"])
    try:
        WebDriverWait(context.driver, 3).until(
            EC.invisibility_of_element_located((by_badge, loc_badge))
        )
    except TimeoutException:
        raise AssertionError("Cart badge still visible after reset")

    by_add, loc_add = parse_locator(INVENTORY_PAGE["add_to_cart_buttons"])
    add_buttons = context.driver.find_elements(by_add, loc_add)
    assert len(add_buttons) > 0, "No Add to cart buttons found after reset"

    by_sort, loc_sort = parse_locator(INVENTORY_PAGE["sort_dropdown"])
    dropdown = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((by_sort, loc_sort))
    )
    selected = Select(dropdown).first_selected_option.text.strip()
    assert selected == "Name (A to Z)", f"Unexpected default sort: {selected}"

@when('I click "About"')
def step_click_about(context):
    by, loc = parse_locator(INVENTORY_PAGE["about_button"])
    wait_and_click(context.driver, by, loc)

@then("I should be redirected to the About page")
def step_redirected_to_about_page(context):
    current_url = context.driver.current_url.lower()
    assert "saucelabs.com" in current_url, \
        f"Unexpected URL: {current_url}"

@when("I click the Twitter footer link")
def step_click_twitter_footer_link(context):
    by, loc = parse_locator(FOOTER_LINKS["twitter"])
    context._orig_window = click_and_switch_to_new_tab(context.driver, by, loc)

@then("I should be redirected to the Twitter page")
def step_redirected_to_twitter_page(context):
    url = context.driver.current_url.lower()
    assert "x.com" in url, f"Unexpected URL: {url}"
    close_tab_and_switch_back(context.driver, context._orig_window)

@when("I click the Facebook footer link")
def step_click_facebook_footer_link(context):
    by, loc = parse_locator(FOOTER_LINKS["facebook"])
    context._orig_window = click_and_switch_to_new_tab(context.driver, by, loc)

@then("I should be redirected to the Facebook page")
def step_redirected_to_facebook_page(context):
    url = context.driver.current_url.lower()
    assert "facebook.com" in url, f"Unexpected URL: {url}"
    close_tab_and_switch_back(context.driver, context._orig_window)

@when("I click the LinkedIn footer link")
def step_click_linkedin_footer_link(context):
    by, loc = parse_locator(FOOTER_LINKS["linkedin"])
    context._orig_window = click_and_switch_to_new_tab(context.driver, by, loc)

@then("I should be redirected to the LinkedIn page")
def step_redirected_to_linkedin_page(context):
    url = context.driver.current_url.lower()
    assert "linkedin.com" in url, f"Unexpected URL: {url}"
    close_tab_and_switch_back(context.driver, context._orig_window)