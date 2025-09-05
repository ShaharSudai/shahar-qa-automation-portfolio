Feature: Navigation across the application

  Background:
    Given I am logged in to the SauceDemo application

  Scenario: Navigate to cart from header icon
    When I click the cart icon
    Then I should be redirected to the cart page

  Scenario: Return to inventory from the cart
    When I open the cart page
    And I click "Continue Shopping"
    Then I should be redirected to the inventory page

  Scenario: Open a product details page and go back
    When I open the first product details
    Then I should see the product details page
    When I click the back to products button
    Then I should be redirected to the inventory page

  Scenario: Open side menu and navigate to All Items
    When I open the side menu
    And I click "All Items"
    Then I should be redirected to the inventory page

  Scenario: Open side menu and reset app state
    When I open the side menu
    And I click "Reset App State"
    Then the cart icon should show 0 items
    And the inventory should be in default state

  Scenario: Open About from side menu
    When I open the side menu
    And I click "About"
    Then I should be redirected to the About page

  Scenario: Open Twitter link from footer
    When I click the Twitter footer link
    Then I should be redirected to the Twitter page

  Scenario: Open Facebook link from footer
    When I click the Facebook footer link
    Then I should be redirected to the Facebook page

  Scenario: Open LinkedIn link from footer
    When I click the LinkedIn footer link
    Then I should be redirected to the LinkedIn page
