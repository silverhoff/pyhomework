class Grouphelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create_new_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()
        self.fill_group_form(group)
        self.new_group_submit()
        self.open_group_page_again()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def new_group_submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def group_update_submit(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def open_group_page_again(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.open_group_page_again()

    def modify(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        self.group_update_submit()
        self.open_group_page_again()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))




