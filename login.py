# -*- coding: utf-8 -*-
from application import Application
import pytest, time


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tearDown)
    return fixture

#
# def test_login(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("alpikin63@gmail.com", '123456Qa!')
#     app.logout()

# def test_empty_pass(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("alpikin63@gmail.com", '')
#     assert app.driver.find_element_by_id("authPassword-error").text == "поле необходимо заполнить"
#     assert app.driver.find_element_by_id("authPassword-error").is_displayed()
#
# def test_empty_login(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("", '123456Qa!')
#     assert app.driver.find_element_by_id("authEmail-error").text == "поле необходимо заполнить"
#     assert app.driver.find_element_by_id("authEmail-error").is_displayed()
#
#
# def test_empty_login_pass(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("", '')
#     assert app.driver.find_element_by_id("authEmail-error").text == "поле необходимо заполнить"
#     assert app.driver.find_element_by_id("authEmail-error").is_displayed()
#     assert app.driver.find_element_by_id("authPassword-error").text == "поле необходимо заполнить"
#     assert app.driver.find_element_by_id("authPassword-error").is_displayed()
#
#
# def test_incorrect_login(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("sdfsdfsdfsdf", '')
#     assert app.driver.find_element_by_id(
#         "authEmail-error").text == "пожалуйста, введите корректный адрес электронной почты"
#     assert app.driver.find_element_by_id("authEmail-error").is_displayed()
#
# def test_short_pass(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("alpikin63@gmail.com", '1234')
#     assert app.driver.find_element_by_id(
#         "authEmail-error").text == "не менее 6 символов"
#     assert app.driver.find_element_by_id("authPassword-error").is_displayed()


def test_wronglogin(app):
    app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
    app.open_authorization_form()
    app.authorization("asdalpikin63@gmail.com", '123456Qa!')
    time.sleep(5)
    print(app.driver.find_element_by_css_selector(
        "#authEmail+div.error-message span").text)
    assert app.driver.find_element_by_css_selector(
        "#authEmail+div.error-message span").text == '"Пользователь с таким e-mail не зарегистрирован." Регистрация'
    assert app.driver.find_element_by_id("authPassword-error").is_displayed()


# def test_wrongpass(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("alpikin63@gmail.com", '123456Qad!')

