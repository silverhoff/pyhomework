from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, companyname=None, companyaddress=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None,firstmail=None, secondmail=None, thirdmail=None, homepage=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.companyname = companyname
        self.companyaddress = companyaddress
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.firstmail = firstmail
        self.secondmail = secondmail
        self.thirdmail = thirdmail
        self.homepage = homepage
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize