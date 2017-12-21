# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest

def test_secondtest(app, db, json_contacts, check_ui):
    contact = json_contacts
    with pytest.allure.step('Given a group contact'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('I add a contact %s to the list' % contact):
        app.contact.open_new()
        app.contact.fill_data(contact)
        app.contact.submit_new()
        app.contact.open_home()
    with pytest.allure.step('the new contact list equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        if check_ui:
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)