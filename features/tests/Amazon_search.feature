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

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened

  Scenario: 'Your Amazon Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify 'Your Amazon Cart is empty' text present


  Scenario: Amazon Music has 7 menu items
    Given Open Amazon page
    When Click on hamburger menu
    And Click on Amazon Music menu item
    Then 7 menu items are present


  Scenario: User can select from dropdown and search in department
    Given Open Amazon page
    When Select Electronics department
    And Search for Tablet
    Then Verify electronics department is selected