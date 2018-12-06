from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)

    def open_page(self, url):
        self.driver.get(url)

    def logout(self):
        #WebDriverWait(self.driver, 10).until(
            #EC.invisibility_of_element_located((By.CSS_SELECTOR, ".page-header__top-row-item.page-header__top-row-item--user.tooltip.js-tooltip")))
        self.driver.find_element_by_css_selector(
            ".page-header__top-row-item.page-header__top-row-item--user.tooltip.js-tooltip").click()
        self.driver.find_element_by_link_text("Выход").click()

    def authorization(self, login, password):
        self.driver.find_element_by_id("authEmail").click()
        self.driver.find_element_by_id("authEmail").clear()
        self.driver.find_element_by_id("authEmail").send_keys(login)
        self.driver.find_element_by_id("authPassword").clear()
        self.driver.find_element_by_id("authPassword").send_keys(password)
        self.driver.find_element_by_css_selector(".popup-authorization .btn.btn--colored.js-submit").click()

    def open_authorization_form(self):
        self.driver.find_element_by_css_selector(
            ".page-header__top-row-item.page-header__top-row-item--user.tooltip.js-tooltip").click()
        self.driver.find_element_by_css_selector(".page-header__login-menu-enter.btn.btn--colored.js-modal").click()

    def tearDown(self):
        self.driver.quit()
