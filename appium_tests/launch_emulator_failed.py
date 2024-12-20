from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

import time

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

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

login_btn = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Login'))
login_btn.click()

enter_email = wait.until(
    lambda x: x.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et4"]'))
enter_email.send_keys('Mayday, Mayday, yeah you really drive me crazy')

enter_password = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Et5'))
enter_password.send_keys('Mayday ay ay yeah')

button = wait.until(
    lambda x: x.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/Btn3"]'))
button.click()

time.sleep(5)
driver.quit()

appium_service.stop()
