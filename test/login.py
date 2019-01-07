# -*- coding: utf-8 -*-
import time


def test_login(app):
    app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
    app.open_authorization_form()
    app.session.authorization_interface("alpikin63@gmail.com", '123456Qa!')
    app.session.logout_interface()


def test_empty_pass(app):
    app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
    app.open_authorization_form()
    app.session.authorization_interface("alpikin63@gmail.com", '')
    assert app.driver.find_element_by_id("authPassword-error").text == "поле необходимо заполнить"
    assert app.driver.find_element_by_id("authPassword-error").is_displayed()


def test_empty_login(app):
    app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
    app.open_authorization_form()
    app.session.authorization_interface("", '123456Qa!')
    assert app.driver.find_element_by_id("authEmail-error").text == "поле необходимо заполнить"
    assert app.driver.find_element_by_id("authEmail-error").is_displayed()


def test_empty_login_pass(app):
    app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
    app.open_authorization_form()
    app.session.authorization_interface("", '')
    assert app.driver.find_element_by_id("authEmail-error").text == "поле необходимо заполнить"
    assert app.driver.find_element_by_id("authEmail-error").is_displayed()
    assert app.driver.find_element_by_id("authPassword-error").text == "поле необходимо заполнить"
    assert app.driver.find_element_by_id("authPassword-error").is_displayed()


def test_incorrect_login(app):
    app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
    app.open_authorization_form()
    app.session.authorization_interface("sdfsdfsdfsdf", '')
    assert app.driver.find_element_by_id(
        "authEmail-error").text == "пожалуйста, введите корректный адрес электронной почты"
    assert app.driver.find_element_by_id("authEmail-error").is_displayed()

def test_short_pass(app):
    app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
    app.open_authorization_form()
    app.session.authorization_interface("alpikin63@gmail.com", '1234')
    assert app.driver.find_element_by_id(
        "authPassword-error").text == "не менее 6 символов"
    assert app.driver.find_element_by_id("authPassword-error").is_displayed()


def test_wronglogin(app):
    app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
    app.open_authorization_form()
    app.session.authorization_interface("asdalpikin63@gmail.com", '123456Qa!')
    time.sleep(5)
    a = app.driver.find_element_by_css_selector(
        "#authEmail+div.error-message span").text

    print(a.rindex("Пользователь с таким e-mail не зарегистрирован"))
    assert app.driver.find_element_by_css_selector(
        "#authEmail+div.error-message span").text == "Пользователь с таким e-mail не зарегистрирован. Регистрация"
    assert app.driver.find_element_by_id("authPassword-error").is_displayed()


# def test_wrongpass(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization_interface("alpikin63@gmail.com", '123456Qad!')

