# Created by romanshcherbakov at 10/9/20
Feature: Test Search feature


  Scenario: User can search for Cancelling an order on Amazon
    Given Open Amazon Help page
    When Input Cancel Order into Amazon Help search field
    Then First Help result contains Cancel Items or Orders