# Created by romanshcherbakov at 10/2/20
Feature: Test Amazon Search
  # Enter feature description here

  Scenario: Amazon search returns correct results
    Given Open Amazon page
    When Input Shoes into Amazon search field
    And Click on Amazon search icon
    Then First Amazon result contains Shoes

  Scenario: Sign Up disappears
    Given Open Amazon page
    Then Verify Sign In is visible
    When Wait for 9 seconds
    Then Verify Sign In is visible
    And Verify Sign In disappears