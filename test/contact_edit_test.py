from model.contact import Contact

def test_contact_edit_first_part(app):
    if app.contact.count() == 0:
        app.group.create_new_group(Contact(firstname="test"))
    contact = Contact(firstname="Boris", middlename="Borisovich", lastname="Borisov", nickname="Boris122",
                               title="Second contact")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.open_new()
    app.open_home_page()
    app.contact.modify(contact)
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


    #def test_contact_edit_second_part(app):
#    if app.contact.count() == 0:
#        app.group.create_new_group(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.open_new()
#    app.open_home_page()
#    app.contact.modify(Contact(companyname="Second company", companyaddress="321",
#                               homephone="+71111111111", firstmail="test123@mail.ru",
#                               homepage="http://ya.ru"))
#    app.open_home_page()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)