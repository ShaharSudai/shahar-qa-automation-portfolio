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
    "all_items_button": "id=inventory_sidebar_link",
    "reset_app_state_button": "id=reset_sidebar_link",
    "about_button": "id=about_sidebar_link",
    "logout_button": "id=logout_sidebar_link",
    "product_names": "class=inventory_item_name",
    "product_prices": "class=inventory_item_price",
    "first_product_name": "xpath=(//div[@class='inventory_item_name'])[1]",
    "first_product_link": "xpath=(//a[contains(@id,'_title_link')])[1]",
    "first_product_name_div": "xpath=(//div[contains(@class,'inventory_item_name')])[1]",
    "first_add_to_cart_button": "xpath=(//button[contains(text(),'Add to cart')])[1]",
    "first_remove_button": "xpath=(//button[contains(text(),'Remove')])[1]",
    "second_add_to_cart_button": "xpath=(//button[contains(text(),'Add to cart')])[2]",
    "cart_badge": "class=shopping_cart_badge",
    "cart_page_button": "id=shopping_cart_container",
    "add_to_cart_buttons": "xpath=//button[text()='Add to cart']",
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

PRODUCT_PAGE = {
    "product_name": "class=inventory_details_name",
    "back_button": "id=back-to-products"
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
    "overview_title": "css=.title",
    "overview_item_names": "class=inventory_item_name",
    "overview_item_prices": "class=inventory_item_price",
    "item_total_label": "css=.summary_subtotal_label",
    "tax_label": "css=.summary_tax_label",
    "total_label": "css=.summary_total_label",
    "cancel_button_step_two": "id=cancel",
    "finish_button": "id=finish",
    "back_home_button": "id=back-to-products"
}

CHECKOUT_COMPLETE_PAGE = {
    "complete_title": "css=.title",
    "confirmation_header": "css=.complete-header",
    "confirmation_text": "css=.complete-text"
}

FOOTER_LINKS = {
    "twitter": "css=.social_twitter a",
    "facebook": "css=.social_facebook a",
    "linkedin": "css=.social_linkedin a"
}