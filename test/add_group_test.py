# -*- coding: utf-8 -*-
from model.group import Group



def test_firsttest(app):

    #app.session.login(username="admin", password="secret")
    app.group.fill_data(Group(name="ftft", header="tftf", footer="tegvetr"))
    #app.session.logout()

def test_firsttest_empty_group(app):
    #app.session.login(username="admin", password="secret")
    app.group.fill_data(Group(name="", header="", footer=""))
    #app.session.logout()