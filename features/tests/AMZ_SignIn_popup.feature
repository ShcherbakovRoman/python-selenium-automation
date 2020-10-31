# Created by romanshcherbakov at 10/30/20
Feature: Amazon Main page
  # Enter feature description here

  Scenario: Sign In pop up disappears
    Given Open Amazon home page
    Then Sign In pop up is present and clickable
    When Sign In pop up disappears
    Then Verify Sign In is not clickable
