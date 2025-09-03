LOGIN_PAGE = {
    "username_field": "id=user-name",
    "password_field": "id=password",
    "login_button": "id=login-button",
    "error_message": "xpath=//h3[@data-test='error']"
}

INVENTORY_PAGE = {
    "page_title": "css=.title",
    "product_list": "class=inventory_item_name",
    "side_menu": "class=bm-burger-button",
    "logout_button": "id=logout_sidebar_link",
    "product_names": "class=inventory_item_name",
    "product_prices": "class=inventory_item_price",
    "first_product_name": "xpath=(//div[@class='inventory_item_name'])[1]",
    "first_add_to_cart_button": "xpath=(//button[contains(text(),'Add to cart')])[1]",
    "first_remove_button": "xpath=(//button[contains(text(),'Remove')])[1]",
    "second_add_to_cart_button": "xpath=(//button[contains(text(),'Add to cart')])[2]",
    "cart_badge": "class=shopping_cart_badge",
    "cart_page_button": "id=shopping_cart_container",
    "sort_dropdown": "class=product_sort_container"
}

CART_PAGE = {
    "cart_title": "css=.title",
    "cart_items": "class=cart_item",
    "cart_badge": "class=shopping_cart_badge",
    "cart_item_names":  "class=inventory_item_name",
    "cart_item_prices": "class=inventory_item_price",
    "cart_item_quantities":"class=cart_quantity",
    "first_remove_button": "xpath=(//button[contains(text(),'Remove')])[1]",
    "continue_shopping_button": "xpath=(//button[contains(text(),'Continue Shopping')])",
    "checkout_button": "xpath=(//button[contains(text(),'Checkout')])"

}

CHECKOUT_PAGE = {
    "checkout_title": "css=.title",
    "continue_button": "id=continue",
    "cancel_button": "id=cancel",
    "error_message": "css=h3[data-test='error']",
    "first_name_field": "id=first-name",
    "last_name_field": "id=last-name",
    "postal_code_field": "id=postal-code"
}

CHECKOUT_OVERVIEW_PAGE = {
    "overview_title": "css=.title"
}