# driver/driver_manager.py
from appium import webdriver
from config.desired_caps import DesiredCapsConfig
from appium.options.ios import XCUITestOptions

class DriverManager:
    driver = None  # Static variable to share driver instance

    @classmethod
    def start_driver(cls):
        """Start Appium Driver and connect to iOS physical device"""
        if cls.driver is None:
           desired_caps = DesiredCapsConfig.get_ios_desired_caps()
           options = XCUITestOptions()
           options.load_capabilities(desired_caps)
           cls.driver = webdriver.Remote(
               command_executor='http://127.0.0.1:4723/wd/hub',
               options=options
           )
           # Set implicit wait (waits for element loading, unit: seconds)
           cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """Shut down Driver and release resources"""
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None


