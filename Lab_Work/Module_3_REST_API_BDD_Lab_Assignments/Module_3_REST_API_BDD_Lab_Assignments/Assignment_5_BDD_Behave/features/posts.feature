Feature: Posts API

  Scenario: Retrieve post 1
    Given the posts API is available
    When I request post 1
    Then the response status should be 200
    And the response should contain post id 1
