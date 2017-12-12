from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random
from random import randrange

dab = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db, check_ui):
    if app.contact.count() == 0:
        app.open_home_page()
        app.contact.open_new()
        app.contact.fill_data(Contact(firstname="Igor"))
        app.contact.submit_new()
    group = (random.choice(db.get_group_list()))
    print (group)
    old_contacts = dab.get_contacts_in_group(group)
    index = randrange(len(db.get_contact_list()))
    contact = old_contacts[index]
    app.contact.open_home()
    app.contact.select_contact_by_id(contact.id)
    app.contact.add_to_group(group.name)
    new_contacts = dab.get_contacts_in_group(group)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)