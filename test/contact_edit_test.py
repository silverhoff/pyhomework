from model.contact import Contact

def test_contact_edit(app):
    app.open_home_page()
    #app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Boris", middlename="Borisovich", lastname="Borisov", nickname="Boris122",
                                  title="Second contact", companyname="Second company", companyaddress="321",
                                  homephone="+71111111111", firstmail="test123@mail.ru",
                                  homepage="http://ya.ru"))
    app.open_home_page()
    # app.session.logout()