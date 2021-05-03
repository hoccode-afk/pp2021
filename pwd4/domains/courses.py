#! usr/bin/python3

class Course:
    def __init__(self, main, cid, cname,credit):
        self.cid = cid
        self.cname = cname
        self.credit = credit
        Main.courses.append(self)
        Main.courses_id.append(self.cid)

    def get_cid(self):
        return self.cid
    def get_cname(self):
        return self.cname
    def get_credit(self):
        return self.credit
