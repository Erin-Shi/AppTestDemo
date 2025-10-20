# config/desired_caps.py
class DesiredCapsConfig:
    @staticmethod
    def get_ios_desired_caps():
        return {
            "platformName": "iOS",  # Fixed as "iOS" for iOS platform
            "platformVersion": "16.7.12",  # iPhone OS version (must match device, e.g., 16.5)
            "deviceName": "testPhone",  # Custom device name (matches iTunes display)
            "udid": "7432c2f5431ea4bbe6243cfaafb51bc3165969cb",  # iPhone UDID (found in Settings > General > About)
            "bundleId": "locspc",  # Target app's Bundle ID (e.g., WeChat: com.tencent.xin)
            # Replace bundleId with "app": "/path/to/your/app.ipa" if installing local IPA
            "automationName": "XCUITest",  # Fixed as "XCUITest" for iOS automation
            "noReset": True,  # Do not reset app data (avoids re-login on each launch)
            "autoAcceptAlerts": True,  # Auto-accept system alerts (e.g., permission requests)
            "useNewWDA": False,  # Reuse WDA (speeds up launch; set to True for first use)
            "wdaLocalPort": 8100  # WDA port (default 8100; change for multiple devices)
        }