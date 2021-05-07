""" 
    PW3
    name: 3.student.mark.oop.math.py
    Use math module
    Use numpy
        Calculate GPA for given student
        Sort student list by GPA descending
    Decorate UI
"""


# ! usr/bin/python3
import math
import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    

# Driver class
class Driver():
    # Class variable
    # List to store information of students
    students = []
    # List to store information of courses
    courses = []
    # List to store information of marks
    marks = []

    # Class variable
    nofstudents = None
    nofcourses = None

    ##### Input functions (5)

    # Function to input number of students
    def input_number_students(self):
        while True:
            try:
                self.nofstudents = int(input("Enter number of students: "))
                while self.nofstudents <= 0:
                    print("Number of students has to be positive integer!!!\n")
                    self.nofstudents = int(input("Enter again number of students: "))
            except:
                print("Number of students has to be positive integer!!!\n")
            else:
                break

    # Function to input number of courses
    def input_number_courses(self):
        while True:
            try:
                self.nofcourses = int(input("Enter number of courses: "))
                while self.nofcourses <= 0:
                    print("Number of couses has to be positive integer!!!\n")
                    self.nofcourses = int(input("Enter again number of courses: "))
            except:
                print("Number of courses has to be positive integer!!!\n")
            else:
                break


    # Function to input information of students
    def input_students_infor(self):
        if self.nofstudents <= 0:
            print("Student list is empty. Please enter number of students!!!")
        elif self.nofstudents > len(self.students):
            for i in range(0, self.nofstudents):
                print(f"Enter information of student #{i + 1}")
                while True:
                    try:
                        sid = int(input(f"Enter student id: "))
                        while sid <= 0:
                            sid = int(input(f"ID must be positive. Enter again student id: "))
                    except:
                        print("ID has to be positive integer!!!")
                    else:
                        break
                        
                while True:
                    try:
                        sname = input(f"Enter name of student #{sid}: ")
                        while len(sname) == 0:
                            sname = input(f"Student name can't be empty.Enter agian name of student #{sid}: ")
                    except:
                        print(f"Student name can't be empty.Enter agian name of student #{sid}: ")
                    else:
                        break #Still not good!!!Name is still entered by numbers

                while True:
                    try:
                        sdob = input(f"Enter date of birth of student #{sid}: ")
                        while len(sdob) == 0:
                            sdob = input(f"Student name can't be empty.Enter agian name of student #{sid}: ")
                    except:
                        print("Student name can't be empty.Enter again name of student!!!")
                    else:
                        break #Still not good!!!Dob is still entered by letters

                self.students.append(Student(sid, sname, sdob))
        else:
            print(f"The student list is full({len(self.students)} students).Please use function 1 to extra student list")
    

    # Function to input information of courses
    def input_courses_infor(self):
        if self.nofcourses <= 0:
            print("Course list is empty. Please enter number of courses!!!")
        elif self.nofcourses > len(self.courses):
            for i in range(0, self.nofcourses):
                print(f"Enter information of course #{i + 1}")
                while True:
                    try:
                        cid = int(input(f"Enter course id: "))
                        while cid <= 0:
                            cid = int(input(f"Enter again course id: "))
                    except:
                        print("Course id must be positive integer!!!")
                    else:
                        break

                while True:
                    try:    
                        cname = input(f"Enter name of course #{cid}: ")
                        while len(cname) == 0:
                            cname = input(f"Name of course can't be empty.Enter name of course #{cid}: ")
                    except:
                        print(f"Name of course can't be empty.Please enter name of course #{cid}!!! ")
                    else:
                        break

                while True:
                    try:
                        credit = int(input(f"Enter credit of course #{cid}: "))
                        while credit <= 0:
                            credit = int(input(f"Credit of Course is positive.Enter again credit of course: "))
                    except:
                        print(f"Credit of Course is positive.Please enter again credit of course #{cid}!!!")
                    else:
                        break
                self.courses.append(Course(cid, cname, credit))
        else:
            print(f"The list of courses is full({len(self.courses)} courses).Please use function 2 to extra student list")

    # Function to input mark of exactly courses for students
    def input_mark(self):
        while True:
            try:
                cid = int(input("Enter id of course you want to input mark: "))
                while cid <= 0:
                    cid = int(input("Course id must be positive.Enter  again course id you want to input mark: "))
            except:
                print("Course id must be positive.Please enter again course id you want to input mark!!!")
            else:
                break
        for course in self.courses:
            if course.get_cid() == cid:
                for student in self.students:
                    while True:
                        try:
                            value = float(input(f"Enter mark of course {cid} for student {student.get_sname()}: "))
                            while value < 0:
                                value = float(input("Mark must not be negative\n " \
                                                   f"Enter again mark of course {cid} for student {student.get_sname()}: "))
                        except:
                            print("Mark must not be negative\n " \
                                 f"Enter again mark of course {cid} for student {student.get_sname()}!!!")
                        else:
                            break
                    #Round-down student scores to 1-digit decimal 
                    value = math.floor(value * 10)/10.0

                    self.marks.append(Mark(student, course, value))
            else:
                print("Course id is not existed!!!") 
  
    
    # Function to calculate GPA for given student
    def calculate_GPA(self):
        while True:
            try:
                sid = int(input(f"Enter student id you want to calculate GPA: "))
                while sid <= 0:
                    sid = int(input(f"ID must be positive. Enter again student id: "))
                
                check = 0
                for mark in self.marks:
                    if check == (len(self.marks) - 1):
                        print(f"Error. Student id {sid} not existed!!!")
                        break
                    elif sid != mark.get_student().get_sid():
                        check = check + 1
                    else:
                        print("Student id is existed!!!")
            except:
                print("ID must be positive. Enter again student id!!!")
            else:
                break

        list_score = np.array([])
        list_credit = np.array([])

        check = 0
        for mark in self.marks:
            if sid == mark.get_student().get_sid():
                list_score = np.append(list_score, mark.get_value())
                list_credit = np.append(list_credit, mark.get_course().get_credit())

        gpa = np.dot(list_score, list_credit) / np.sum(list_credit)

        for student in self.students:
            if sid == student.get_sid():
                student.set_gpa(gpa)

    # Function to sort student list by GPA decrending
    def sort_student_list(self):
        if len(self.students) == 0:
            print("List of student information is empty!!!") 
        else:
            data_type = [('sid', 'S30'), ('sname', 'S30'), ('gpa', float)]
            new_students = []
            for student in self.students:
                new_student_infor = (student.get_sid(), student.get_sname(), student.get_gpa())
                new_students.append(new_student_infor)
            sorting_new_students = np.array(new_students, dtype=data_type)
            sorted_list = np.sort(sorting_new_students, order = 'gpa')
            print(sorted_list)
    #### Display functions (3)

    # Function to list all student's informations
    def list_students(self):
        if len(self.students) == 0:
            print("The student list is empty!!!")
        else:
            print("Student id", "Student name", "Student dob", sep="             ")
            for student in self.students:
                print(f"{student.get_sid()}" ,
                      f"{student.get_sname()}" ,
                      f"{student.get_sdob()}", sep="             ")

    # Function to list all course's informations
    def list_courses(self):
        if len(self.courses) == 0:
            print("The course list is empty!!!")
        else:
            for course in self.courses:
                print(f"Course id: {course.get_cid()}" \
                      f"Course name: {course.get_cname()}", sep=" - ")

    # Function to list student marks for a given course
    def list_mark(self):
        if len(self.marks) == 0:
            print("The mark list is empty!!!")
        else:
            while True:
                try:
                    cid = int(input("Enter id of course you want to list marks: "))
                    while cid <= 0:
                        cid = int(input("Course id must be positive.Enter  again course id you want to list marks: "))
                     
                    check = 0
                    for mark in self.marks:
                        if check == (len(self.marks) - 1):
                            print("Error")
                            break
                        elif cid != mark.get_course().get_cid():
                            check = check + 1
                        else:
                            print("Course id is existed!!!")
                except:
                    print("Course id must be positive.Enter again course id you want to list marks!!!")
                else:
                    break
            for mark in self.marks:
                if cid == mark.get_course().get_cid():
                    print(mark.get_student().get_sname(), mark.get_course().get_cname(), mark.get_value(), sep="-")

    
    # Function to run the program
    def run_Driver(self):
        print("Please select operation: \n"           \
                "1.Input number of students \n"       \
                "2.Input number of courses \n"        \
                "3.Input information for students \n" \
                "4.Input information for courses \n"  \
                "5.Input mark for given courses \n"   \
                "6.Calculate GPA for given student\n" \
                "7.Sort student by gpa\n"             \
                "8.List students \n"                  \
                "9.List courses \n"                   \
                "10.List marks \n"                    \
                "11.Exist!!!" ,  )
        while True:
            select = int(input("Select operations form 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11:"))
            if select == 1:
                self.input_number_students()    
            elif select == 2:
                self.input_number_courses()
            elif select == 3:
                self.input_students_infor()
            elif select == 4:
                self.input_courses_infor()
            elif select == 5:
                self.input_mark()
            elif select == 6:
                self.calculate_GPA()
            elif select == 7:
                self.sort_student_list()
            elif select == 8:
                self.list_students()
            elif select == 9:
                self.list_courses()
            elif select == 10:
                self.list_mark()
            elif select == 11:
                print("Existed!!!")
                break
            else:
                print("Invalid value")
                

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    # Create object driver
    d = Driver()
    d.run_Driver()
