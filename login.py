# -*- coding: utf-8 -*-
from application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tearDown)
    return fixture


def test_untitled_test_case(app):
    app.open_page("http://loginarea:passarea@gap.aeroidea.ru/")
    app.open_authorization_form()
    app.authorization("alpikin63@gmail.com", '123456Qa!')
    app.logout()
