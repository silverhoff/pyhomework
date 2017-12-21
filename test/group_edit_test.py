from model.group import Group
from random import randrange
import pytest


def test_modify_group_name(app, db, check_ui):
    with pytest.allure.step('Check that it is not empty group list'):
        if app.group.count() == 0:
            app.group.create_new_group(Group(name="test"))
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Choose random group'):
        index = randrange(len(old_groups))
        group = Group(name="abc")
        group.id = old_groups[index].id
        app.group.modify_by_index(index, group)
    with pytest.allure.step('I edit a group %s' % group):
        new_groups = app.group.get_group_list()
    with pytest.allure.step('the new group list equal to the old list with the edited group'):
        assert len(old_groups) == len(new_groups)
        old_groups[index] = group
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)