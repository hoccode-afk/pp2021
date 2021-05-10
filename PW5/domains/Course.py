
# Course class - Parent class
class Course:
    # Contructor
    def __init__(self, cid, cname, credit):
        self.cid = cid
        self.cname = cname
        self.credit = credit

    # Get methods
    def get_cid(self):
        return self.cid

    def get_cname(self):
        return self.cname
    
    def get_credit(self):
        return self.credit

     #Set methods
    def set_cname(self, cname):
        self.cname = cname

    def set_cid(self, cid):
        self.cid = cid
    
    def set_credit(self, credit):
        self.credit = credit