# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_secondtest(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_new_contact()
    app.fill_new_contact(Contact(firstname="Ivan", middlename="\\9", lastname="Ivanov", nickname="ivan299",
                              title="Test contact", companyname="Test company", companyaddress="123",
                              homephone="+7000000000", firstmail="test@mail.ru",
                              homepage="http://localhost/addressbook/edit.php"))
    app.submit_new_contact()
    app.open_home()
    app.logout()
