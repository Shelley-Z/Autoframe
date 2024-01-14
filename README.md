# Test Automation Project

## Overview
This project demonstrates API and mobile test automation using Python, Selenium, Appium, and the `requests` library.

## Prerequisites
- Python installed
- Appium installed
- Android or iOS emulator/simulator installed
- Appium server running (`appium` command)

## Setup
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
4. Install dependencies: `pip install -r requirements.txt`

## Running Tests
### API Test
1. Open a terminal.
2. Run: `python api_test.py`

### Mobile Test
1. Ensure the Appium server is running.
2. Open another terminal.
3. Run: `python mobile_test.py`

## Additional Notes
- Adjust device capabilities in `mobile_test.py` based on your emulator/simulator configuration.
- Customize test actions in mobile tests as needed.
- Screenshots are captured for mobile test cases and saved in the "screenshots" folder.
