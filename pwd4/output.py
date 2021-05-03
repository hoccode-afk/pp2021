import numpy as np
import math

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
    print("List all the mark: ")
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