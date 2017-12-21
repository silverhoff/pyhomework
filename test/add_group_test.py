# -*- coding: utf-8 -*-
from model.group import Group
import pytest

def test_add_group(app, db, json_groups):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('I add a group %s to the list' % group):
        app.group.create_new_group(group)
    with pytest.allure.step('the new group list equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
