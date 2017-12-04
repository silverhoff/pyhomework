from model.group import Group
from random import randrange


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="abc")
    group.id = old_groups[index].id
    app.group.modify_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)