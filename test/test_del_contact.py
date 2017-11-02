def test_delete_first_contact(app):
    app.open_home_page()
    app.contact.delete()
    app.open_home_page()