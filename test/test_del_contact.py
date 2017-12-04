from model.contact import Contact
import random

def test_delete_first_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.open_home_page()
        app.contact.open_new()
        app.contact.fill_data(Contact(firstname="Igor"))
        app.contact.submit_new()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.open_home_page()
    app.contact.delete_by_id(contact.id)
    app.open_home_page()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)