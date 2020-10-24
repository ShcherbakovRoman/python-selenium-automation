# Created by romanshcherbakov at 10/23/20
Feature: Use https://www.amazon.com/gp/product/B07BJKRR25/ color selection OR ANY OTHER ITEM.
Create 1 test case that will loop through colors (in any way you prefer)


  Scenario: Color check
    Given Open Amazon product B07BJKRR25 page
    Then Verify all colors are displayed
