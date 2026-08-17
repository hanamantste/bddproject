#noinspection CucumberUndefinedStep
Feature: Login
  Scenario Outline: verify login
    Given user is on login page
    When user enters "<username>" and "<password>"
    And click login button
    Then On Success full login"<text>" is displayed on home page
    Examples:
    |username                     |  password     | text          |
    |ragh.gr89@gmail.com          |  8147151204   | Qafox.com     |
    |Admin                        |  admin123     | Qafox.com1    |


