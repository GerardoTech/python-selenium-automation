Feature: Test sign in navigation when logged out

  Scenario: User is able to get to sign in form
    Given Open Target main page
    When Click Sign in
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened

