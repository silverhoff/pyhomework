# -*- coding: utf-8 -*-
from model.contact import Contact

def test_secondtest(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_new()
    contact = Contact(firstname="Ivan", middlename="\\9", lastname="Ivanov", nickname="ivan299",
                                  title="Test contact", companyname="Test company", companyaddress="123",
                                  homephone="+7000000000", firstmail="test@mail.ru",
                                  homepage="http://localhost/addressbook/edit.php")
    app.contact.fill_data(contact)
    app.contact.submit_new()
    app.contact.open_home()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


