def test_wrong_email(app):
    app.open_page()
    app.session.open_authorization_form()
    app.session.open_fogotpass_form()
    app.driver.find_element_by_id('forgotEmail').click()
    app.driver.find_element_by_id('forgotEmail').clear()
    app.driver.find_element_by_id('forgotEmail').send_keys('test@test.qa')