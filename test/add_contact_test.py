# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                                  title=random_string("title", 10), companyname=random_string("companyname", 10), companyaddress=random_string("companyaddress", 10),
                                  homephone=random_string("homephone", 11), mobilephone=random_string("mobilephone", 11), workphone=random_string("workphone", 11), secondaryphone=random_string("secondaryphone", 10), firstmail=random_string("firstmail", 10),
                                  secondmail=random_string("secondmail", 10), thirdmail=random_string("thirdmail", 10),
                                  homepage=random_string("homepage", 10))
                                                     for i in range(3)
            ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_secondtest(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_new()
    app.contact.fill_data(contact)
    app.contact.submit_new()
    app.contact.open_home()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)