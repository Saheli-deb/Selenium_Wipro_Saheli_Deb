Feature: Posts API data driven scenarios

  @smoke
  Scenario Outline: Retrieve a post
    When I request post <id>
    Then the response status should be 200

    Examples:
      | id |
      | 1  |
      | 2  |
      | 3  |
