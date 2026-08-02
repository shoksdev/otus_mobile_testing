import pytest
from appium import webdriver
from appium.options.common import AppiumOptions



@pytest.fixture()
def driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        # "appium:app": "C:/Users/User/Downloads/pnv.apk"
    })

    appium_server_url = 'http://localhost:4723'
    android_driver = webdriver.Remote(appium_server_url, options=options)
    yield android_driver
    android_driver.quit()
