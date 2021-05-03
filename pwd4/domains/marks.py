#! usr/bin/python3

class Mark():
    def __init__(self, main, sid, cid, value):
        self.value = value
        self.cid = cid
        self.sid = sid
        Main.marks.append(self)

    def get_value(self):
        return self.value
    def get_cid(self):
        return self.cid
    def get_sid(self):
        return self.sid