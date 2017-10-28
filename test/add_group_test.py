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
    app.login(username="admin", password="secret")
    app.fill_data_new_group(Group(name="ftft", header="tftf", footer="tegvetr"))
    app.logout()

def test_firsttest_empty_group(app):
    app.login(username="admin", password="secret")
    app.fill_data_new_group(Group(name="", header="", footer=""))
    app.logout()