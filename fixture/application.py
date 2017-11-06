from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import Sessionhelper
from fixture.group import Grouphelper
from fixture.contact import Contacthelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = Sessionhelper(self)
        self.group = Grouphelper(self)
        self.contact = Contacthelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
