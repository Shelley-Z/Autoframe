import unittest
from appium import webdriver
from PIL import Image
from io import BytesIO

class MobileTest(unittest.TestCase):

    def setUp(self):
        # Appium server details
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.android.calculator2',
            'appActivity': '.Calculator',
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_positive_mobile(self):
        # Perform positive mobile test actions
        # Example: Calculate 2 + 2
        self.perform_calculator_operation(2, '+', 2)

        # Capture screenshot for positive test
        self.capture_screenshot("mobile_test_positive")

    def test_negative_mobile(self):
        # Perform negative mobile test actions
        # Example: Divide by zero
        self.perform_calculator_operation(5, '/', 0)

        # Capture screenshot for negative test
        self.capture_screenshot("mobile_test_negative")

    def perform_calculator_operation(self, operand1, operator, operand2):
        # Perform calculator operation
        self.driver.find_element_by_id(f"digit_{operand1}").click()
        self.driver.find_element_by_accessibility_id(operator).click()
        self.driver.find_element_by_id(f"digit_{operand2}").click()
        self.driver.find_element_by_id("eq").click()

    def capture_screenshot(self, test_name):
        # Capture screenshot and save to screenshots folder
        screenshot_path = f"screenshots/{test_name}.png"
        screenshot = self.driver.get_screenshot_as_png()
        Image.open(BytesIO(screenshot)).save(screenshot_path)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
