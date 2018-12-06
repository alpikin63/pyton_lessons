# -*- coding: utf-8 -*-
from application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tearDown)
    return fixture


def test_login(app):
    app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
    app.open_authorization_form()
    app.authorization("alpikin63@gmail.com", '123456Qa!')
    app.logout()

# def test_empty_pass(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("alpikin63@gmail.com", '')
#
# def test_empty_login(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("", '123456Qa!')
#
# def test_empty_login_pass(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("", '')
#
# def test_wronglogin(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("asdalpikin63@gmail.com", '123456Qa!')
#
# def test_wrongpass(app):
#     app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
#     app.open_authorization_form()
#     app.authorization("alpikin63@gmail.com", '123456Qad!')

