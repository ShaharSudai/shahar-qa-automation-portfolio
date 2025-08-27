Feature: Logout functionality

  Background:
    Given I am logged in to the SauceDemo application

  Scenario: Successful logout
    When I open the side menu
    And I click the logout link
    Then I should be redirected back to the login page
    And I should see the login button
