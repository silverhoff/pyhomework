from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random
from random import randrange
import pytest

dab = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_remove_contact_from_group(app, db):
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
    with pytest.allure.step('Given a group list'):
        old_contacts = dab.get_contacts_in_group(group)
    with pytest.allure.step('Add contact to group if there is no contacts in group %s' % group):
        if not old_contacts:
            app.open_home_page()
            contacts = db.get_contact_list()
            index = randrange(len(contacts))
            contact = contacts[index]
            app.contact.select_contact_by_id(contact.id)
            app.contact.add_to_group(group.name)
            old_contacts = dab.get_contacts_in_group(group)
        else:
            index = randrange(len(old_contacts))
            contact = old_contacts[index]
    with pytest.allure.step('Delete contact %s from group %s ' % (contact, group)):
        app.contact.delete_contact_from_group(contact, group.id)
    with pytest.allure.step('the new group list equal to the old list without deleted contact from the group'):
        new_contacts = dab.get_contacts_in_group(group)
        old_contacts.remove(contact)
        print(old_contacts,new_contacts)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

