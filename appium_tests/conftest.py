import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService


@pytest.fixture()
def appium_driver():
    appium_service = AppiumService()
    appium_service.start()

    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "platformVersion": "10",
        "deviceName": "Pixel5",
        "udid": "emulator-5554",
        "app": r"C:\Program Files\Testing_Appium_Selenium\Android_Demo_App_V2.apk",
        "appPackage": "com.code2lead.kwad",
        "appActivity": "com.code2lead.kwad.MainActivity"
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)

    yield driver

    driver.quit()
    appium_service.stop()
