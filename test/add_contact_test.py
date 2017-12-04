# -*- coding: utf-8 -*-
from model.contact import Contact

def test_secondtest(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.open_new()
    app.contact.fill_data(contact)
    app.contact.submit_new()
    app.contact.open_home()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)