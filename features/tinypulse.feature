Feature: TINYpulse

  Scenario: Login to system then adding some users
    Given We are on the TINYpulse login page
    When We login by entering username & password
    Then We successfully login to system
    When We click on Settings icon in bottom right side-bar
    And We click on Add People
    And We add 2 users into list
    Then We verify Congratulations page displays


  Scenario Outline: Verify error display when by left required fields blank
    Given We are on the TINYpulse login page
    When We login by entering username & password
    Then We successfully login to system
    When We click on Settings icon in bottom right side-bar
    And We click on Add People
    And We add <condition> into list
    Then We verify an error will display

    Examples:
      | condition                 |
      | 1 user without first name |
      | 1 user without last name  |
      | 1 user without email      |