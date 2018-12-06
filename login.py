# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://loginarea:passarea@gap.aeroidea.ru/")

    def test_untitled_test_case(self):
        driver = self.driver
        self.open_authorization_form(driver)
        self.authorization(driver, "alpikin63@gmail.com", '123456Qa!')
        self.unauthorization(driver)

    def unauthorization(self, driver):
        driver.find_element_by_css_selector(
            ".page-header__top-row-item.page-header__top-row-item--user.tooltip.js-tooltip").click()
        driver.find_element_by_link_text("Выход").click()

    def authorization(self, driver, login, password):
        driver.find_element_by_id("authEmail").click()
        driver.find_element_by_id("authEmail").clear()
        driver.find_element_by_id("authEmail").send_keys(login)
        driver.find_element_by_id("authPassword").clear()
        driver.find_element_by_id("authPassword").send_keys(password)
        driver.find_element_by_css_selector(".popup-authorization .btn.btn--colored.js-submit").click()
        time.sleep(5)

    def open_authorization_form(self, driver):
        driver.find_element_by_css_selector(
            ".page-header__top-row-item.page-header__top-row-item--user.tooltip.js-tooltip").click()
        driver.find_element_by_css_selector(".page-header__login-menu-enter.btn.btn--colored.js-modal").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
