# Created by romanshcherbakov at 10/30/20
Feature: Amazon Best Sellers tabs

  Scenario: Check all tabs under Best Sellers
    Given Open Amazon home page
    When Click Best Sellers
    Then Click on each top link and verify that new page opens