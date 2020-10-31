# Created by romanshcherbakov at 10/30/20
Feature: Window handling

  Scenario: Company's website is opened in a new tab
    Given Open Yelp page
    When Click on a web-site link
    And Switch to a new window
    Then The Restaurnat's website is opened
    And User can close new window and return to original window
