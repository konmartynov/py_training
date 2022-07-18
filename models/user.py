

class User:

    def __init__(self, fname=None, mname=None, lname=None, nickname=None, company=None, address=None,
                 home_phone=None, mobile=None, work_phone=None, fax=None, email=None, note=None, id=None,
                 second_phone=None):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile = mobile
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.note = note
        self.id = id
        self.second_phone = second_phone

    def __repr__(self):
        return "%s:%s" % self.id, self.fname, self.lname

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.fname == other.fname \
               and self.lname == other.lname

    def sort_lname(self):
        if self.lname:
            return str(self.lname)
