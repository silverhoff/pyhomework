from model.group import Group


def test_modify_group_name(app):
    #app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="abc"))
    #app.session.logout()

def test_modify_group_header(app):
    #app.session.login(username="admin", password="secret")
    app.group.modify(Group(header="cba"))
    #app.session.logout()