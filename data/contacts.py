from model.contact import Contact
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                                  title=random_string("title", 10), companyname=random_string("companyname", 10), companyaddress=random_string("companyaddress", 10),
                                  homephone=random_string("homephone", 11), mobilephone=random_string("mobilephone", 11), workphone=random_string("workphone", 11), secondaryphone=random_string("secondaryphone", 10), firstmail=random_string("firstmail", 10),
                                  secondmail=random_string("secondmail", 10), thirdmail=random_string("thirdmail", 10),
                                  homepage=random_string("homepage", 10))
                                                     for i in range(n)
            ]