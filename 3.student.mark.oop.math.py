#! usr/bin/python3

import numpy as np
import math

class Student:
    def __init__(self, main, sid, sname, sdob,gpa=0):
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

class Main:
    #List to store students information
    students = []
    #List to store student id
    students_id = []
    #List to store courses information
    courses = []
    #List to store id of courses
    courses_id = []
    #List to store marks with given course
    marks = []
    
    nofstudent = None
    nofcourse = None


    #Input number of students by user:
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

    #List all the courses:
    def list_courses(self):
        print("List all the courses: ")
        for course in self.courses:
            print(f"Course {course.get_cid()} : {course.get_cname()}")

    #List all the student:
    def list_students(self):
        print("List all the student")
        for student in self.students:
            print(f"Student id : {student.get_sid()} \t Student name : {student.get_sname()} \t Student dob : {student.get_sdob()} \t")

    #List all the mark:
    def list_marks(self):
        cid = int(input("Enter the course id you want print mark: "))
        print("List all the marks: ")
        for mark in self.marks:
            if mark.get_cid() == cid:
                sid = mark.get_sid()
                for student in self.students:
                    if student.get_sid() == sid:
                        print(f"Student id : {student.get_sid()} \t Student name : {student.get_sname()} \t Mark : {mark.get_value()}")

    
    def cal_GPA(self):
        mark = np.array([])
        credit = np.array([])

        sid = input("Id of student you want to calculate GPA: ")
        for student in self.students:
            if student.get_sid() == sid:
                for mark in self.marks:
                    if mark.get_sid() == sid:
                        for course in self.courses:
                            if course.get_cid() == mark.get_cid():
                                mark = np.append(mark, mark.get_value())
                                credit = np.append(credit, course.get_credit())
        
        gpa = np.dot(mark, credit) / np.sum(credit)
        rounded_gpa = math.floor(gpa * 10)/10.0
        for student in self.students:
            if student.get_sid() == sid:
                student.get_gpa(rounded_gpa)
    
    def sort_print_student_gpa(self):
        dtype = [('sid', 'S10'), ('name', 'S25'), ('gpa', float)]
        new_student_infor_list = []
        for student in self.students:
            self.cal_GPA()
            new_student_infor = (student.get.sid(), student.get_sname(), student.get_gpa())
            new_student_infor_list.append(new_student_infor)

        sorted_list = np.array(new_student_infor_list, dtype=dtype)      
        np.sort(sorted_list, order='gpa') 
        print(sorted_list)

    def run_main(self):
        m.input_number_course()
        m.input_number_student()
        m.input_student_infor()
        m.input_course_infor()
        m.input_course_mark()
        m.list_courses()
        m.list_students()
        m.list_marks()
        m.cal_GPA()
        m.sort_print_student_gpa()

if __name__ == '__main__':
    m = Main()
    m.run_main()