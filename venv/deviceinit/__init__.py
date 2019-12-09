import os
from appium import webdriver
from time import sleep
import unittest


class DeviceInit(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '9.0', 'deviceName': 'Mi A2 Lite',
                        'appPackage': 'com.maguru.app'}
        # desired_caps['appActivity'] = '.activityName'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def loginScreen(self):
        el = self.driver.find_element_by_link_text("Indtast dit telefonnummer")
        el.click()


