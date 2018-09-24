# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from  time import sleep
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def Authorization(self):
        success = True
        wd = self.wd
        wd.get("http://10.128.55.34:8080")
        wd.find_element_by_id("id_username").click()
        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys("admin")
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys("admin")
        wd.find_element_by_css_selector("button[type=\"submit\"]").click()




    def tearDown (self):
        self.wd.quit()