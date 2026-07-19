import time

import pytest
import allure
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


@allure.feature("Swipe Test")
@allure.story("Swipe to Camera")
def test_scroll(driver):
    previous_names = None

    while True:
        with allure.step("Поиск элементов"):
            elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
            element_names = [name.text for name in elements]

        with allure.step("Проверка на наличие Calendar и нажатие, если он найден"):
            if 'Calendar' in element_names:
                element = driver.find_element(AppiumBy.XPATH,
                                              '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.csdroid.pkg:id/recycler"]/android.widget.FrameLayout[4]')
                element.click()
                break

        if previous_names is not None and element_names == previous_names:
            raise AssertionError("Конец списка! Calendar не найден!")

        with allure.step("Выполнение свайпа"):
            driver.swipe(elements[1].rect['x'], elements[1].rect['y'],
                         elements[0].rect['x'], elements[0].rect['y'])

        time.sleep(1.0) # Ожидание в секунду, иначе возникает разрыв соеденения из-за слишком частых запросов
        previous_names = element_names


