Feature: Checkout Flow
  Login to the e-commerce site as a valid customer and add products to cart.
  Navigate to the cart page and complete the checkout flow

  Scenario: End-to-end checkout flow
    Given User is on the login page
    When User enters a username "standard_user" and password "secret_sauce" and logs in
    Then User navigates to the inventory page

    Given User navigates to the product page for "Sauce Labs Backpack"
    When User adds the product to cart
    Then Button text on the page should change to "Remove"
    And User navigates back to the inventory page

    Given User navigates to the product page for "Sauce Labs Bike Light"
    When User adds the product to cart
    Then Button text on the page should change to "Remove"
    And User navigates back to the inventory page

    When User navigates to the cart page
    Then User should be on the cart page
    And The cart should contain product "Sauce Labs Backpack"
    And The cart should contain product "Sauce Labs Bike Light"
    And The cart item count should be "2"
    And The checkout button text should be "Checkout"

    When User clicks on the checkout button
    Then User should be on the checkout step one page
    When User enters first name "Peter", last name "Hanks", and zip code "12345"
    Then The field values should be firstname "Peter", lastname "Hanks", and zip code "12345"

    When User clicks on the continue checkout button
    Then User should be on the checkout step two page
    Then The payment info should be "SauceCard #31337"
    And The shipping info should be "Free Pony Express Delivery!"
    And The total should be "Total: $86.38"

    When User finishes checking out
    Then User sees completion message and order completion text