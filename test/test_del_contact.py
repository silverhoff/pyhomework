from model.contact import Contact
from random import randrange

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.open_home_page()
        app.contact.open_new()
        app.contact.fill_data(Contact(firstname="Igor"))
        app.contact.submit_new()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.open_home_page()
    app.contact.delete_by_index(index)
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts