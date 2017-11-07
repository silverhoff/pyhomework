# -*- coding: utf-8 -*-
from model.group import Group


def test_firsttest(app):
    old_groups = app.group.get_group_list()
    app.group.create_new_group(Group(name="ftft", header="tftf", footer="tegvetr"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_firsttest_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new_group(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
