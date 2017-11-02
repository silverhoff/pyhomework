# -*- coding: utf-8 -*-
from model.group import Group


def test_firsttest(app):
    app.group.create_new_group(Group(name="ftft", header="tftf", footer="tegvetr"))

def test_firsttest_empty_group(app):
    app.group.create_new_group(Group(name="", header="", footer=""))
