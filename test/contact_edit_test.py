from model.contact import Contact

def test_contact_edit_first_part(app):
    if app.contact.count() == 0:
        app.group.create_new_group(Contact(firstname="test"))
    app.open_home_page()
    app.contact.modify(Contact(firstname="Boris", middlename="Borisovich", lastname="Borisov", nickname="Boris122",
                               title="Second contact"))
    app.open_home_page()

def test_contact_edit_second_part(app):
    if app.contact.count() == 0:
        app.group.create_new_group(Contact(firstname="test"))
    app.open_home_page()
    app.contact.modify(Contact(companyname="Second company", companyaddress="321",
                               homephone="+71111111111", firstmail="test123@mail.ru",
                               homepage="http://ya.ru"))
    app.open_home_page()