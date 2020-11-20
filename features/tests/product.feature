# Created by romanshcherbakov at 11/20/20
Feature: Features on product page

  Scenario: Tooltip is displayed when hover over Add to Cart
    Given Open Amazon product B074TBCSC8 page
    When Hover over Add to Cart button
    Then Verify if tooltip is being displayed


  Scenario: New Arrivals are displayed when hover over
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals link
    Then Verify if deals are displayed