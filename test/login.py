# -*- coding: utf-8 -*-


def test_login(app):
    app.open_page(app.base_url)
    app.session.open_authorization_form()
    app.session.authorization_interface("alpikin63@gmail.com", '123456Qa!')
    app.session.logout_interface()


def test_empty_pass(app):
    app.open_page(app.base_url)
    app.session.open_authorization_form()
    app.session.authorization_interface("alpikin63@gmail.com", '')
    assert app.driver.find_element_by_id(app.session.pass_error_id).text == "поле необходимо заполнить"
    assert app.driver.find_element_by_id(app.session.pass_error_id).is_displayed()


def test_empty_login(app):
    app.open_page(app.base_url)
    app.session.open_authorization_form()
    app.session.authorization_interface("", '123456Qa!')
    assert app.driver.find_element_by_id(app.session.email_error_id).text == "поле необходимо заполнить"
    assert app.driver.find_element_by_id("authEmail-error").is_displayed()


def test_empty_login_pass(app):
    app.open_page(app.base_url)
    app.session.open_authorization_form()
    app.session.authorization_interface("", '')
    assert app.driver.find_element_by_id(app.session.email_error_id).text == "поле необходимо заполнить"
    assert app.driver.find_element_by_id(app.session.email_error_id).is_displayed()
    assert app.driver.find_element_by_id(app.session.pass_error_id).text == "поле необходимо заполнить"
    assert app.driver.find_element_by_id(app.session.pass_error_id).is_displayed()


def test_incorrect_login(app):
    app.open_page(app.base_url)
    app.session.open_authorization_form()
    app.session.authorization_interface("wrong_emaeil", '')
    assert app.driver.find_element_by_id(
        app.session.email_error_id).text == "пожалуйста, введите корректный адрес электронной почты"
    assert app.driver.find_element_by_id(app.session.email_error_id).is_displayed()


def test_short_pass(app):
    app.open_page(app.base_url)
    app.session.open_authorization_form()
    app.session.authorization_interface("alpikin63@gmail.com", '1234')
    assert app.driver.find_element_by_id(
        app.session.pass_error_id).text == "не менее 6 символов"
    assert app.driver.find_element_by_id(app.session.pass_error_id).is_displayed()


def test_wronglogin(app):
    app.open_page(app.base_url)
    app.session.open_authorization_form()
    app.session.authorization_interface("asdalpikin63@gmail.com", '123456Qa!')
    app.wait_by_css(5, app.session.email_error_css)
    assert app.driver.find_element_by_css_selector(
        app.session.email_error_css).text == "Пользователь с таким e-mail не зарегистрирован. Регистрация"
    app.driver.find_element_by_css_selector(app.session.email_error_css + " a").click()
    app.wait_by_name(5, "registration-email")
    assert app.driver.find_element_by_name("registration-email").get_attribute("value") == 'asdalpikin63@gmail.com'


def test_wrongpass(app):
    app.open_page(app.base_url)
    app.session.open_authorization_form()
    app.session.authorization_interface("alpikin63@gmail.com", '123456Qad!')
    app.wait_by_css(5, app.session.pass_error_css)
    assert app.driver.find_element_by_css_selector(
        app.session.pass_error_css).text == "Пароль неверный, попробуйте еще раз"
