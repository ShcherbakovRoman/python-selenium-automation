# Created by romanshcherbakov at 10/16/20
Feature: Search for product and add it to Cart
  Add any product you want into the cart, and make sure it’s there
  (check for the number of items in the cart OR open the cart and verify it’s there)


  Scenario: Amazon search and add product to Cart
    Given Open new Amazon page
    When Input Flashlight into Amazon search field and search for it
    And Add any product to Cart
    Then Confirm this product is added to Cart