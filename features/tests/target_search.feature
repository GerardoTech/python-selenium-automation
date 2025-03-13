Feature: Target search test cases

  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results show