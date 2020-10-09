# Created by romanshcherbakov at 10/9/20
Feature: Test the cart is empty
  # Enter feature description here

  Scenario: Verify that Your Shopping Cart is empty.
    Given Open Amazon home page
    When Click on Cart icon
    Then Verify Cart is empty