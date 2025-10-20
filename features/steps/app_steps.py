# features/steps/app_steps.py
from behave import given, when, then
from driver.driver_manager import DriverManager
from appium.webdriver.common.appiumby import AppiumBy
from hamcrest import assert_that, equal_to

# Global variable: Store API endpoint retrieved from the page
global_api_endpoint = None

@given("Launch the app and enter the home page")
def step_impl(context):
    """Start the driver and open the app's home page"""
    context.driver = DriverManager.start_driver()  # Store driver in context for other steps

@when('Click the "{btn_name}" button (accessibility id: {accessibility_id})')
def step_impl(context, btn_name, accessibility_id):
    print(f"{accessibility_id}")
    menu_btn = context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=accessibility_id)
    menu_btn.click()

@then('Expend "{menu_name}"')
def step_impl(context, page_title, accessibility_id):
    print(f"{menu_name}")
    menu_xpath = "//XCUIElementTypeOther[@name='{menu_name}']"
    menu_element = context.driver.find_element(by=AppiumBy.xpath, value=menu_xpath)
    menu_element.click()



