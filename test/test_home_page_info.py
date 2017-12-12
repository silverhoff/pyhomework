import re
from model.contact import Contact

def test_home_page_info(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    for n in range (len(contacts_from_home_page)):
        contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)[n]
        contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)[n]
        assert contacts_from_home_page.firstname == contacts_from_db.firstname
        assert contacts_from_home_page.lastname == contacts_from_db.lastname
        assert contacts_from_home_page.companyaddress == contacts_from_db.companyaddress
        assert contacts_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db)
        assert contacts_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db)


'''def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone'''

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
        filter(lambda x : x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x : x is not None, [contact.firstmail, contact.secondmail, contact.thirdmail])))