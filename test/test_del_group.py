from model.group import Group
import random
import pytest

def test_delete_some_group(app, db, check_ui):
    with pytest.allure.step('Check that it is not empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create_new_group(Group(name="test"))
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Choose random group'):
        group = random.choice(old_groups)
    with pytest.allure.step('Delete group %s' % group):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('the new group list equal to the old list without the deleted group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == app.group.count()
        old_groups.remove(group)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)