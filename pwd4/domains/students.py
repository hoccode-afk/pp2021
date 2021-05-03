#! usr/bin/python3

class Student:
    def __init__(self, main, sid, sname, sdob, gpa=0):
        self.sid = sid
        self.sname = sname
        self.sdob = sdob
        self.gpa = gpa
        Main.students.append(self)
        Main.students_id.append(self.sid)

    def get_sid(self):
        return self.sid

    def get_sname(self):
        return self.sname

    def get_sdob(self):
        return self.sdob

    def set_gpa(self, gpa):
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

