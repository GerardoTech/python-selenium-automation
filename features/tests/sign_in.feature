Feature: Sign in test


  Scenario: Verify user can get to sign in page
    Given Open target main page
    When Click on 'Sign in' Button
    When Click on 'Sign in' Button on pop up
    Then Verify sign in page opens