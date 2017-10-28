# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_secondtest(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_new()
    app.contact.fill_data(Contact(firstname="Ivan", middlename="\\9", lastname="Ivanov", nickname="ivan299",
                                  title="Test contact", companyname="Test company", companyaddress="123",
                                  homephone="+7000000000", firstmail="test@mail.ru",
                                  homepage="http://localhost/addressbook/edit.php"))
    app.contact.submit_new()
    app.contact.open_home()
    app.session.logout()
