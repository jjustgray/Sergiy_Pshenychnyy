Feature: Dropbox test

  Scenario: Upload Delete
    Given we upload file
    When we check file name
    Then we remove file
