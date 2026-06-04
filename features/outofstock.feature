

Feature: Out of Stock
  Scenario: Verify searching with out of stock product
    Given user is on login page
    When  user enters username and password
    And   click on login
    And   search not in stock product
    Then  should display out of stock product marked are not available
