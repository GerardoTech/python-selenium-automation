Feature: Target search test cases

#  Scenario: User can search for a product on Target
#    Given Open target main page
#    When Search for tea
#    Then Verify correct search results shown for tea


  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Search for <search_word>
    Then Verify correct search results shown for <expected_text>
    Examples:
    |search_word  |expected_text
    |tea          |tea
    |dress        |dress
    |iphone       |iphone

