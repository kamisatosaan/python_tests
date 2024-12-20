from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

import time


def test_launch_emulator_failed(appium_driver):
    driver = appium_driver

    email_text = 'Mayday, Mayday, yeah you really drive me crazy'
    password_text = 'Mayday ay ay yeah'

    wait = WebDriverWait(driver, 25, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                             NoSuchElementException])

    login_btn = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Login'))
    login_btn.click()

    enter_email = wait.until(
        lambda x: x.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et4"]'))
    enter_email.send_keys(email_text)

    enter_password = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Et5'))
    enter_password.send_keys(password_text)

    button = wait.until(
        lambda x: x.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/Btn3"]'))
    button.click()

    assert enter_email.text == email_text
    assert enter_password.text == password_text

    time.sleep(5)


def test_launch_emulator_passed(appium_driver):
    driver = appium_driver

    email_text = 'admin@gmail.com'
    password_text = 'admin123'
    enter_admin_text = 'enter admin text'

    wait = WebDriverWait(driver, 25, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                             NoSuchElementException])

    login_btn = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Login'))
    login_btn.click()

    enter_email = wait.until(
        lambda x: x.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et4"]'))
    enter_email.send_keys(email_text)

    enter_password = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Et5'))
    enter_password.send_keys(password_text)

    button = wait.until(
        lambda x: x.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/Btn3"]'))
    button.click()

    enter_admin = wait.until(lambda x: x.find_element(AppiumBy.XPATH,
                                                      '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Edt_admin"]'))
    enter_admin.send_keys(enter_admin_text)

    submit_btn = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Btn_admin_sub'))
    submit_btn.click()

    preview = wait.until(lambda x: x.find_element(AppiumBy.XPATH,
                                                  '//android.widget.TextView[@resource-id="com.code2lead.kwad:id/Tv_admin"]'))
    assert preview.text == enter_admin_text

    time.sleep(5)
