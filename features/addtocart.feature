Feature: Add to cart
  Scenario: Adding to Cart and checkout
    Given user is on login page
    When user enter product to search product
    And  click on search button
    When respective product should be displayed
    When user clicks add to cart
    When user checkout
    Then billing page should be displayed
