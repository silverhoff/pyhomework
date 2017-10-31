from model.group import Group


def test_first_group_edition(app):

    #app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="abc", header="abc", footer="abc"))
    #app.session.logout()