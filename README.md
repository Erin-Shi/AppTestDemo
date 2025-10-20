This is a simple app test demo with two scenario:
1) Click menu to get the 9-Day Forecast via appium web driver agent.
   Launch the app
   CLick the menu button on the left panel
   Expend the menu "Forcast & Warning Services"
   Click the menu "9-Day Forecast"
2) Get humidity for the day after tomorrow via http request.
   Send a GET request
   Verify the API response status is "success"
   Get humidity for the day after tomorrow

Prepare:
  pip3 install -r requirements.txt
Execution:
  For scenario 1
    behave --no-capture-stdout  features/app_operation.feature
    * I don't have the apple developer account. The Appium WebDriverAgent couldn't work correctly on iphone. So I couldn't debug the sctipts.
  For scenario 2
    pytest -s tests/test_app_basic.py    
    behave --no-capture-stdout  features/api_operation.feature 
