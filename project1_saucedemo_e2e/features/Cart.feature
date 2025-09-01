Feature: Cart page functionality

  Background:
    Given I am logged in to the SauceDemo application

  Scenario: View empty cart
    When I open the cart page
    Then the cart should be empty
    And the cart icon should show 0 items

  Scenario: Add one product and see it in the cart
    Given I have added a product to the cart
    When I open the cart page
    Then I should see that product in the cart
    And the cart icon should show 1 item

  Scenario: Add multiple products and see them in the cart
    Given I have added 2 products to the cart
    When I open the cart page
    Then I should see 2 cart items
    And each cart item should have a name and a price
    And each cart item should have a quantity

  Scenario: Remove a product from the cart page
    Given I have added a product to the cart
    When I open the cart page
    And I remove that product from the cart
    Then the cart should be empty
    And the cart icon should show 0 items

  Scenario: Continue shopping from the cart
    Given I have added a product to the cart
    When I open the cart page
    And I click "Continue Shopping"
    Then I should be redirected to the inventory page

  Scenario: Proceed to checkout from the cart
    Given I have added a product to the cart
    When I open the cart page
    And I click "Checkout"
    Then I should be redirected to the checkout step one page
