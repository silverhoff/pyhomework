from model.contact import Contact
import random
import pytest

def test_delete_first_contact(app, db, check_ui):
    with pytest.allure.step('Check that it is not empty contact list'):
        if app.contact.count() == 0:
            app.open_home_page()
            app.contact.open_new()
            app.contact.fill_data(Contact(firstname="Igor"))
            app.contact.submit_new()
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Choose random contact'):
        contact = random.choice(old_contacts)
    with pytest.allure.step('Delete contact %s' % contact):
        app.open_home_page()
        app.contact.delete_by_id(contact.id)
        app.open_home_page()
    with pytest.allure.step('the new contact list equal to the old list without the deleted contact'):
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        if check_ui:
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)