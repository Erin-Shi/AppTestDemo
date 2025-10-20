# utils/api_request.py
import requests
from requests.exceptions import RequestException

class ApiRequest:
    @staticmethod
    def send_get(url, params=None, headers=None):
        """Send a GET request"""
        try:
            response = requests.get(
                url=url,
                params=params,
                headers=headers,
                timeout=10  # Timeout to prevent infinite waiting
            )
            response.raise_for_status()  # Raise exception if status code is not 200
            return response
        except RequestException as e:
            raise Exception(f"GET request failed: {str(e)}")

    @staticmethod
    def send_post(url, data=None, json=None, headers=None):
        """Send a POST request"""
        try:
            response = requests.post(
                url=url,
                data=data,
                json=json,
                headers=headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise Exception(f"POST request failed: {str(e)}")