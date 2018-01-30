Feature: Implement a calculator
  Scenario: User ads two numbers
    Given I have the number 20
    And I have the numer 30
    When I sum the numbers
    Then The result should be 50