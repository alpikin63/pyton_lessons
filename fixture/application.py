from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    base_url = 'http://gap.aeroidea.ru/'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.session = SessionHelper(self)

    def open_page(self, url, http_log='loginarea', http_pass='passarea'):
        index = url.rfind('//')
        new_url = url[:index+2] + http_log + ':' + http_pass + '@' + url[index+2:]
        self.driver.get(new_url)

    def tear_down(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False
