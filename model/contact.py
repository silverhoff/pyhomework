class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, companyname=None, companyaddress=None,
                         homephone=None, firstmail=None, homepage=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.companyname = companyname
        self.companyaddress = companyaddress
        self.homephone = homephone
        self.firstmail = firstmail
        self.homepage = homepage
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname and self.lastname == other.lastname