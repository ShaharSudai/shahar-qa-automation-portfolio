Feature: Checkout flow

  Background:
    Given I am logged in to the SauceDemo application
    And I have added a product to the cart
    When I open the cart page

  # Step One (Your Information)
  Scenario: Proceed to checkout step one
    When I click "Checkout"
    Then I should be redirected to the checkout step one page

  Scenario: Validation - missing first name
    When I click "Checkout"
    And I continue without filling the first name
    Then I should see an error message that first name is required

  Scenario: Validation - missing last name
    When I click "Checkout"
    And I continue without filling the last name
    Then I should see an error message that last name is required

  Scenario: Validation - missing postal code
    When I click "Checkout"
    And I continue without filling the postal code
    Then I should see an error message that postal code is required

  Scenario: Cancel from step one returns to cart
    When I click "Checkout"
    And I click "Cancel" on checkout step one
    Then I should be redirected to the cart page

  Scenario: Continue to step two with valid information
    When I click "Checkout"
    And I fill valid checkout information
    And I click "Continue"
    Then I should be redirected to the checkout overview page

  # Step Two (Overview)
  Scenario: Overview shows selected items and accurate item total
    When I click "Checkout"
    And I fill valid checkout information
    And I click "Continue"
    Then I should see the selected items in the overview
    And the item total should equal the sum of item prices

  Scenario: Overview shows tax and total calculation
    When I click "Checkout"
    And I fill valid checkout information
    And I click "Continue"
    Then I should see a tax amount
    And the total should equal item total plus tax

  Scenario: Cancel from step two returns to inventory
    When I click "Checkout"
    And I fill valid checkout information
    And I click "Continue"
    And I click "Cancel" on checkout step two
    Then I should be redirected to the inventory page

  # Complete
  Scenario: Finish order successfully
    When I click "Checkout"
    And I fill valid checkout information
    And I click "Continue"
    And I click "Finish"
    Then I should be redirected to the checkout complete page
    And I should see a confirmation message for the order

  Scenario: Back home from complete returns to inventory
    When I click "Checkout"
    And I fill valid checkout information
    And I click "Continue"
    And I click "Finish"
    And I click "Back Home"
    Then I should be redirected to the inventory page
