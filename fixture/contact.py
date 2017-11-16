from model.contact import Contact

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
        self.change_field_value("email", contact.firstmail)
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

    def modify(self):
        self.modify_by_index(0)

    def modify_by_index(self, index, contact):
        wd = self.app.wd
        edit_contact = wd.find_elements_by_name("entry")
        cells = edit_contact[index].find_elements_by_tag_name("td")
        cells[7].click()
        self.fill_data(contact)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

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
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)