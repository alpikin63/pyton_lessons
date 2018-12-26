from selenium import webdriver
from fixture.session import SessionHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Application:

    base_url = 'http://st.gap.aeroidea.ru/'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.session = SessionHelper(self)

    def open_page(self, url, http_log='loginarea', http_pass='passarea'):
        index = url.rfind('//')
        new_url = url[:index+2] + http_log + ':' + http_pass + '@' + url[index+2:]
        self.driver.get(new_url)

    def wait_by_id(self, delay, id_locator):
        wait_elem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.ID, id_locator)))
        return wait_elem

    def wait_by_css(self, delay, css_locator):
        wait_elem = WebDriverWait(self.driver, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_locator)))
        return wait_elem

    def wait_by_css_enable(self, delay, css_locator):
        wait_elem = WebDriverWait(self.driver, delay).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_locator)))
        return wait_elem

    def wait_by_name(self, delay, name_locator):
        wait_elem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.NAME, name_locator)))
        return wait_elem

    def wait_by_link(self, delay, link_locator):
        wait_elem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((
            By.LINK_TEXT, link_locator)))
        return wait_elem

    def tear_down(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False
