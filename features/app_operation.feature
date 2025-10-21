# features/app_operation.feature
Feature: App Operation
  Test menu clicking

  Scenario: Click menu
    Given Launch the app
    When Click "Menu" (accessibility id: Menu, left side panel)
    Then Expend "Forcast & Warning Services"
    And Click "9-Day Forecast" (accessibility id: 9-Day Forecast)
