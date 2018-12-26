
class SessionHelper:

    email_id = "authEmail"
    pass_id = "authPassword"
    login_modal_css = ".popup-authorization.modal .btn"
    header_menu_open_css = ".page-header__top-row-item--user .page-header__top-row-text"
    auth_enter_css = ".tooltip__window .page-header__login-menu-enter"
    email_error_id = 'authEmail-error'
    pass_error_id = 'authPassword-error'
    email_error_css = '#authEmail+div.error-message span'
    pass_error_css = '#authPassword+div.error-message span'

    def __init__(self, app):
        self.app = app

    def open_authorization_form(self):
        driver = self.app.driver
        driver.find_element_by_css_selector(self.header_menu_open_css).click()
        driver.find_element_by_css_selector(self.auth_enter_css).click()

    def authorization_interface(self, login, password):
        driver = self.app.driver
        driver.find_element_by_id(self.email_id).click()
        driver.find_element_by_id(self.email_id).clear()
        driver.find_element_by_id(self.email_id).send_keys(login)
        driver.find_element_by_id(self.pass_id).clear()
        driver.find_element_by_id(self.pass_id).send_keys(password)
        driver.find_element_by_css_selector(self.login_modal_css).click()

    def logout_interface(self):
        self.app.wait_by_link(5, 'Мой аккаунт')
        driver = self.app.driver
        driver.find_element_by_css_selector(self.header_menu_open_css).click()
        driver.find_element_by_link_text("Выход").click()

    def logout(self):
        url = self.app.driver.current_url
        self.app.driver.get(url+'?logout=yes')

