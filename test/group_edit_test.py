from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify(Group(name="abc"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify(Group(header="cba"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)