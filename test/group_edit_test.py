from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="test"))
    app.group.modify(Group(name="abc"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="test"))
    app.group.modify(Group(header="cba"))