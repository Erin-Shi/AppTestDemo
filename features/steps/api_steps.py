# features/steps/api_steps.py
from behave import given, when, then
from behave.runner import Context  # 正确导入Context类
from utils.api_request import ApiRequest
from typing import Dict, Optional
import json
from datetime import datetime, timedelta

# Setup steps (Given)
@given('The target API is "{api_url}"')
def step_impl(context: Context, api_url: str):
    context.api_url = api_url

@when('Send a GET request')
def step_impl(context):
    context.api_response = ApiRequest.send_get(url=context.api_url)
    context.status_code = context.api_response.status_code

@then('Verify the API response status is "success"')
def step_impl(context):
    assert context.status_code == 200, f"Expected status 200, got {context.status_code}"

@then('Get humidity for the day after tomorrow')
def step_impl(context):
    current_date = datetime.now()
    day_after_tomorrow = current_date + timedelta(days=2)
    format_date = day_after_tomorrow.strftime("%Y%m%d")
    response_json = context.api_response.json()
    forecast_list = response_json.get('forecast_detail', [])
    for forecast in forecast_list:
        if forecast.get("forecast_date") == format_date:
            max_rh = forecast.get('max_rh')
            min_rh = forecast.get('min_rh')
            print(f"The humidity for {format_date} is {min_rh} - {max_rh}")
            print(f"----------------------------")
            break
    else:
        print(f"Not find the weather forecast")

