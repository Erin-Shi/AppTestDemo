# tests/test_app_basic.py
import pytest
from driver.driver_manager import DriverManager
from appium.webdriver.common.appiumby import AppiumBy
from utils.api_request import ApiRequest
from datetime import datetime, timedelta
from typing import Dict, Optional
import json

class TestAppBasic:
    @classmethod
    def setup_class(cls):
        """Class-level setup: Start the driver"""
        #cls.driver = DriverManager.start_driver()
        cls.api = ApiRequest()

    @classmethod
    def teardown_class(cls):
        """Class-level teardown: Shut down the driver"""
        DriverManager.quit_driver()

    def test_get_api_and_send_request(self):
        current_date = datetime.now()
        day_after_tomorrow = current_date + timedelta(days=2)
        format_date = day_after_tomorrow.strftime("%Y%m%d")

        response = ApiRequest.send_get(url="https://pda.weather.gov.hk/locspc/data/fnd_e.xml")
        response_json = response.json()
        forecast_list = response_json.get("forecast_detail", [])

        for forecast in forecast_list:
            if forecast.get("forecast_date") == format_date:
                max_rh = forecast.get("max_rh")
                min_rh = forecast.get("min_rh")
                print(f"The humidity for {format_date} is {min_rh} - {max_rh}")
                break
        else:
            print(f"Not find the weather forecast")

        assert len(forecast_list) > 0, "No forecast data found!"