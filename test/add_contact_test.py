# -*- coding: utf-8 -*-
from model.contact import Contact

def test_secondtest(app,json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.open_new()
    app.contact.fill_data(contact)
    app.contact.submit_new()
    app.contact.open_home()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)