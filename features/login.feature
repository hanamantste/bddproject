#noinspection CucumberUndefinedStep
Feature: Login
  Scenario Outline: verify login
    Given user is on login page
    When user enters "<username>" and "<password>"
    And click login button
    Then land on home page
    Examples:
    |username                     |password|
    |ragh.gr89@gmail.com          | 8147151204    |
    |Admin          |  admin123    |


