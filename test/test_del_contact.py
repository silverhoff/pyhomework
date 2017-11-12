from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.group.create_new_group(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.open_new()
    app.open_home_page()
    app.contact.delete()
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)  == len(new_contacts)