from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random
from random import randrange

dab = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_remove_contact_from_group(app, db):
    if app.contact.count() == 0:
        app.open_home_page()
        app.contact.open_new()
        app.contact.fill_data(Contact(firstname="Igor"))
        app.contact.submit_new()
    if len(db.get_group_list()) == 0:
        app.group.create_new_group(Group(name="test"))
    group = (random.choice(db.get_group_list()))
    old_contacts = dab.get_contacts_in_group(group)
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
    app.contact.delete_contact_from_group(contact, group.id)
    new_contacts = dab.get_contacts_in_group(group)
    old_contacts.remove(contact)
    print(old_contacts,new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

