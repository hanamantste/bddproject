Feature: Search

  Background:
    Given user is on login page
  @smoke
  Scenario Outline:Search and verify field

    When user enter "<product>" to search product
    And  click on search button
    Then respective product should be displayed "<message>"
    Examples:
    |product|message|
    |Maruti     | There is no product that matches the search criteria.|
    |Honda  |There is no product that matches the search criteria.|

  @smoke
  Scenario: Search valid product
#    Given user is on login page
    When user enter product to search product
    And  click on search button
    Then respective product should be displayed
