from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.group.create_new_group(Contact(firstname="test"))
    app.open_home_page()
    app.contact.delete()
    app.open_home_page()