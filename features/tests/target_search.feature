Feature: Test Target Search Functionality


  Scenario: User can search for coffee
    Given Open Target main page
    When Search for a coffee
    Then Verify that correct search results shown for coffee


  Scenario: User can search for tea
    Given Open Target main page
    When Search for a tea
    Then Verify that correct search results shown for tea


    Scenario: User can search for pillow
    Given Open Target main page
    When Search for a pillow
    Then Verify that correct search results shown for pillow


  Scenario Outline: User can search for product
    Given Open Target main page
    When Search for <search_word>
    Then Verify that correct search results shown for <search_result>
    Examples:
    |search_word    |search_result  |
    |coffee         |coffee         |
    |mug            |mug            |
    |champagne      |champagne      |
    |tortillas      |tortillas      |