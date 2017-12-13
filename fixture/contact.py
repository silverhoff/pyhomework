from model.contact import Contact
from fixture import group
from random import randrange
import re

class Contacthelper:

    def __init__(self, app):
        self.app = app

    def open_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//*[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def submit_new(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_data(self, contact):
        # fill data for new contact
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.companyname)
        self.change_field_value("address", contact.companyaddress)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.firstmail)
        self.change_field_value("email2", contact.secondmail)
        self.change_field_value("email3", contact.thirdmail)
        self.change_field_value("homepage", contact.homepage)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def modify(self):
        self.modify_by_index(0)

    def modify_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_data(contact)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None


    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                companyaddress = cells[3].text
                all_emails = cells[4].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,companyaddress=companyaddress, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        companyaddress = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        firstmail = wd.find_element_by_name("email").get_attribute("value")
        secondmail = wd.find_element_by_name("email2").get_attribute("value")
        thirdmail = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, companyaddress=companyaddress,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                       firstmail=firstmail, secondmail=secondmail, thirdmail=thirdmail)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        edit_contact = wd.find_elements_by_name("entry")
        cells = edit_contact[index].find_elements_by_tag_name("td")
        cells[7].click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        edit_contact = wd.find_elements_by_name("entry")
        cells = edit_contact[index].find_elements_by_tag_name("td")
        cells[6].click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone,mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def select_group_to_show(self, groupname):
        wd = self.app.wd
        wd.find_element_by_name('group').click()
        wd.find_element_by_xpath("//option[contains(text(),'%s')]" % groupname).click()

    def add_to_group(self, groupname):
        wd = self.app.wd
        group = wd.find_elements_by_xpath("//option[contains(text(),'%s')]" % groupname)
        group[-1].click()
        wd.find_element_by_name('add').click()