# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://loginarea:passarea@st.gap.aeroidea.ru/")

    def test_untitled_test_case(self):
        driver = self.driver
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробнее'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Войти'])[1]/following::a[1]").click()
        driver.find_element_by_id("authEmail").click()
        driver.find_element_by_id("authEmail").clear()
        driver.find_element_by_id("authEmail").send_keys("alpikin63@gmail.com")
        driver.find_element_by_id("authPassword").clear()
        driver.find_element_by_id("authPassword").send_keys("123456Qa!")
        # driver.find_element_by_link_text(u"войти").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='Подробнее'])[1]/following::span[1]").click()
        # driver.find_element_by_link_text(u"Выход").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
