# ! usr/bin/python3

# Mark class - Child class
class Mark():
    # Contructor
    def __init__(self, student, course, value):
        self.student = student
        self.course = course
        self.value = value

    # Get methods
    def get_value(self):
        return self.value

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course