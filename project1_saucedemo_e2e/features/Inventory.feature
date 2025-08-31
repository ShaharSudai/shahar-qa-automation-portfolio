Feature: Inventory page functionality

  Background:
    Given I am logged in to the SauceDemo application

  Scenario: View list of products
    When I am on the inventory page
    Then I should see a list of products
    And each product should have a name and a price

  Scenario: Add a product to the cart
    When I click on "Add to cart" for a product
    Then the cart icon should show 1 item

  Scenario: Remove a product from the cart
    Given I have added a product to the cart
    When I click on "Remove" for that product
    Then the cart icon should show no number

  Scenario: Sort products by price (low to high)
    When I sort the products by "Price (low to high)"
    Then the first product should be the cheapest
    And the last product should be the most expensive

  Scenario: Sort products by name (A to Z)
    When I sort the products by "Name (A to Z)"
    Then the first product should start with "A"
