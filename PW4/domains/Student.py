# ! usr/bin/python3

# Student class - Parent class
class Student:
    # Contructor
    def __init__(self, sid, sname, sdob, gpa=0):
        self.sid = sid
        self.sname = sname
        self.sdob = sdob
        self.gpa = gpa
        
    # Get methods
    def get_sid(self):
        return self.sid

    def get_sname(self):
        return self.sname

    def get_sdob(self):
        return self.sdob
    
    def get_gpa(self):
        return self.gpa

    # Set methods
    def set_gpa(self, gpa):
        self.gpa = gpa