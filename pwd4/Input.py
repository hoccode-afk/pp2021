from domains.students import *
from domains.courses import *
from domains.marks import *
from domains.engine import *
import math

class Input:
    def input_number_student(self):
        self.nofstudent = int(input("Enter number of students: "))

    #Input number of courses by user:
    def input_number_course(self):
        self.nofcourse = int(input("Enter number of courses: "))


    #Input information of students:
    def input_student_infor(self):
        for i in range(0, self.nofstudent):
            print(f"Enter information of student {i+1}")
            sid = input(f"Enter student id: ")
            sname = input(f"Enter name of student #{sid}: ")
            sdob = input(f"Enter date of birth of student #{sid}: ")
            gpa = input(f"Enter GPA of student #{sid}: ")
            Student(self, sid, sname, sdob, gpa)

    #Input course informations:
    def input_course_infor(self):
        for i in range(0, self.nofcourse):
            print(f"Enter information of course {i+1}")
            cid = int(input("Enter course id: "))
            cname = input(f"Enter name of course {cid}: ")
            credit = input(f"Enter credit of course {cid}: ")
            Course(self, cid, cname, credit)

    #Input mark for student:
    def input_course_mark(self):
        cid = int(input("Enter the course id you want input mark: "))
        for student in self.students:
            sid = student.get_sid()
            value = float(input(f"Enter mark for {student.get_sname()}: "))
            #Round-down student scores to 1-digit decimal
            math.floor(value)
            Mark(self, sid, cid, value) 




