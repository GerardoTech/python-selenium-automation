Feature: Cart tests

#  Scenario: User receives correct massage for empty cart
#    Given Open Target main page
#    When Click on cart icon
#    Then Verify Your cart is empty message is shown


  Scenario: User can add items to cart
    Given Open Target main page
    When Search for a cup
    And Click add item to shopping cart
    And Confirm add to cart button
    And Open cart page
    Then Verify correct item is in shopping cart