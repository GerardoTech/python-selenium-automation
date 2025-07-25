Feature: Target search test cases

  @smoke
  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results shown for tea
    And Verify tea in URL


#  Scenario Outline: User can search for a product on Target
#    Given Open target main page
#    When Search for <search_word>
#    Then Verify correct search results shown for <expected_text>
#    Examples:
#    |search_word  |expected_text
#    |tea          |tea
#    |dress        |dress
#    |iphone       |iphone

  @smoke
  Scenario: User can add a product to cart
    Given Open target main page
    When Search for chair
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    Then Verify cart has correct product

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image

  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown