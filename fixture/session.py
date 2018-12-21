import time


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def authorization_interface(self, login, password):
        driver = self.app.driver
        driver.find_element_by_id("authEmail").click()
        driver.find_element_by_id("authEmail").clear()
        driver.find_element_by_id("authEmail").send_keys(login)
        driver.find_element_by_id("authPassword").clear()
        driver.find_element_by_id("authPassword").send_keys(password)
        driver.find_element_by_css_selector(".popup-authorization .btn.btn--colored.js-submit").click()

    def logout_interface(self):
        time.sleep(5)
        driver = self.app.driver
        driver.find_element_by_css_selector(
            ".page-header__top-row-item.page-header__top-row-item--user.tooltip.js-tooltip").click()
        driver.find_element_by_link_text("Выход").click()
