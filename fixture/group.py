class Grouphelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create_new_group(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()

    def fill_data(self, group):
        # fill group form
        wd = self.app.wd
        self.create_new_group()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.open_group_page_again()

    def new_group_submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def open_group_page_again(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()