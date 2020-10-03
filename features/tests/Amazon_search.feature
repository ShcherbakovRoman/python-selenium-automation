# Created by romanshcherbakov at 10/2/20
Feature: Test Amazon Search
  # Enter feature description here

  Scenario: Amazon search returns correct results
    Given Open Amazon page
    When Input Shoes into Amazon search field
    And Click on Amazon search icon
    Then First Amazon result contains Shoes