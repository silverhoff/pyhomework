from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random
from random import randrange
import pytest

dab = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db):
    with pytest.allure.step('Check that it is not empty contact list'):
        if app.contact.count() == 0:
            app.open_home_page()
            app.contact.open_new()
            app.contact.fill_data(Contact(firstname="Igor"))
            app.contact.submit_new()
    with pytest.allure.step('Check that it is not empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create_new_group(Group(name="test"))
    with pytest.allure.step('Choose random group'):
        group = (random.choice(db.get_group_list()))
    with pytest.allure.step('Choose random contact'):
        old_contacts = dab.get_contacts_in_group(group)
        contacts = db.get_contact_list()
        index = randrange(len(contacts))
        contact = contacts[index]
    with pytest.allure.step('Check that contact %s not in group %s' % (contact, group)):
        for i in range (len(contacts)):
            if old_contacts.count(contact):
                index = randrange(len(contacts))
                contact = contacts[index]
            else:
                break
        else:
            app.open_home_page()
            app.contact.open_new()
            app.contact.fill_data(Contact(firstname="Igor"))
            app.contact.submit_new()
            contact = sorted(db.get_contact_list(), key=Contact.id_or_max)[-1]
    with pytest.allure.step('Add contact %s in group %s' % (contact, group)):
        app.contact.select_contact_by_id(contact.id)
        app.contact.add_to_group(group.name)
    with pytest.allure.step('the new group list equal to the old list with the added contact to the group'):
        new_contacts = dab.get_contacts_in_group(group)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)