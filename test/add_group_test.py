# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_firsttest(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_data(Group(name="ftft", header="tftf", footer="tegvetr"))
    app.session.logout()

def test_firsttest_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_data(Group(name="", header="", footer=""))
    app.session.logout()