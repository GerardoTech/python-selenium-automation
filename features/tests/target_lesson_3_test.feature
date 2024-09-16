# Created by alexpro at 9/15/24
Feature: Test shopping cart message functionality

  Scenario: User receives correct massage for empty cart
    Given Open Target main page
    When Click on cart icon
    Then Verify Your cart is empty message is shown

Feature: Test sign in navigation when logged out

  Scenario: User is able to get to sign in form
    Given Open Target main page
    When Click Sign in
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened

