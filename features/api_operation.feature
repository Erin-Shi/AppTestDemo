# features/api_operation.feature
Feature: API Humidity Test
  Scenario: Get humidity for the day after tomorrow
    Given The target API is "https://pda.weather.gov.hk/locspc/data/fnd_e.xml"
    When Send a GET request
    Then Verify the API response status is "success"
    And Get humidity for the day after tomorrow

