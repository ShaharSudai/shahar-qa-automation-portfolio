LOGIN_PAGE = {
    "username_field": "id=user-name",
    "password_field": "id=password",
    "login_button": "id=login-button",
    "error_message": "xpath=//h3[@data-test='error']"
}

INVENTORY_PAGE = {
    "page_title": "class=title",
    "product_list": "class=inventory_item_name",
    "side_menu": "class=bm-burger-button",
    "logout_button": "id=logout_sidebar_link",
    "product_names": "class=inventory_item_name",
    "product_prices": "class=inventory_item_price",
    "first_add_to_cart_button": "xpath=(//button[contains(text(),'Add to cart')])[1]",
    "first_remove_button": "xpath=(//button[contains(text(),'Remove')])[1]",
    "cart_badge": "class=shopping_cart_badge",
    "sort_dropdown": "class=product_sort_container"
}