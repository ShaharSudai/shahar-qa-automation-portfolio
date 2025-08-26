Feature: Login functionality
  
  Background:
    Given I am on the SauceDemo login page

  Scenario: Successful login with valid credentials
    When I enter a valid username
    And I enter a valid password
    And I click the login button
    Then I should be redirected to the inventory page
    And I should see the products list

  Scenario: Login with invalid password
    When I enter a valid username
    And I enter an invalid password
    And I click the login button
    Then I should see an error message indicating invalid credentials

  Scenario: Login with locked out user
    When I enter a locked out username
    And I enter a valid password
    And I click the login button
    Then I should see an error message that the user is locked out

  Scenario: Login with empty username and password
    When I click the login button without entering credentials
    Then I should see an error message that username is required

  Scenario: Login with empty password
    When I enter a valid username
    And I leave the password field empty
    And I click the login button
    Then I should see an error message that password is required
