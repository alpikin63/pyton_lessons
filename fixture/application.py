from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.session = SessionHelper(self)

    def open_page(self, url):
        self.driver.get(url)

    def open_authorization_form(self):
        self.driver.find_element_by_css_selector(
            ".page-header__top-row-item.page-header__top-row-item--user.tooltip.js-tooltip").click()
        self.driver.find_element_by_css_selector(".page-header__login-menu-enter.btn.btn--colored.js-modal").click()

    def tearDown(self):
        self.driver.quit()
