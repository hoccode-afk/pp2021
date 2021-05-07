""" PW1
    name: 1.student.mark.py
    Build a student mark management system

    Functions:
        Input functions:
            Input number of students in a class
            Input student information: id, name, DoB
            Input number of courses
            Input course information: id, name
            Select a course, input marks for student in this course
        
        Listing functions:
            List courses
            List students
            Show student marks for a given course

    PW2 
    name: 2.student.mark.oop.py
    Make it OOP
    Same functions
"""


# ! usr/bin/python3


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Student class - Parent class
class Student:
    # Contructor
    def __init__(self, sid, sname, sdob):
        self.sid = sid
        self.sname = sname
        self.sdob = sdob

    # Get methods
    def get_sid(self):
        return self.sid

    def get_sname(self):
        return self.sname

    def get_sdob(self):
        return self.sdob


# Course class - Parent class
class Course:
    # Contructor
    def __init__(self, cid, cname):
        self.cid = cid
        self.cname = cname

    # Get methods
    def get_cid(self):
        return self.cid

    def get_cname(self):
        return self.cname


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
        self.nofstudents = int(input("Enter number of students: "))
        while True:
            if self.nofstudents <= 0:
                print("Invalid value \n" \
                    "Number of students has to be positive integer!!!\n" \
                    "Please enter number of students againt")
                self.input_number_students()
            else:
                break

    # Function to input number of courses
    def input_number_courses(self):
        self.nofcourses = int(input("Enter number of courses: "))
        while True:
            if self.nofcourses <= 0:
                print("Invalid value \n" \
                    "Number of courses has to be positive integer!!!\n" \
                    "Please enter number of courses againt")
                self.input_number_courses()
            else:
                break

    
    # Function to input information of students
    def input_students_infor(self):
        for i in range(0, self.nofstudents):
            print(f"Enter information of student #{i + 1}")

            sid = int(input(f"Enter student id: "))
            while sid <= 0:
                sid = int(input(f"ID must be positive. Enter again student id: "))

            sname = input(f"Enter name of student #{sid}: ")
            while len(sname) == 0:
                sname = input(f"Student name can't be empty.Enter agian name of student #{sid}: ")

            sdob = input(f"Enter date of birth of student #{sid}: ")
            while len(sdob) == 0:
                sdob = input(f"Student date of birth can't be empty.Enter again date of birth of student #{sid}: ")

            self.students.append(Student(sid, sname, sdob))
    

    # Function to input information of courses
    def input_courses_infor(self):
        for i in range(0, self.nofcourses):
            print(f"Enter information of course #{i + 1}")

            cid = int(input(f"Enter course id: "))
            while cid <= 0:
                cid = int(input(f"Course id is positive.Enter again course id: "))
            
            cname = input(f"Enter name of course #{cid}: ")
            while len(cname) == 0:
                cname = input(f"Name of course can't be empty.Enter name of course #{cid}: ")

            self.courses.append(Course(cid, cname))

    # Function to input mark of exactly courses for students
    def input_mark(self):
        cid = int(input("Enter id of course you want to input mark: "))
        while cid <= 0:
            cid = int(input("Course id must be positive.Enter  again course id you want to input mark: "))
        for course in self.courses:
            if course.get_cid() == cid:
                for student in self.students:
                    value = float(input(f"Enter mark of course {cid} for student {student.get_sname()}: "))
                    while value < 0:
                        value = float(input("Mark must not be negative\n " \
                                            f"Enter mark of course {cid} for student {student.get_sname()}: "))

                    self.marks.append(Mark(student, course, value))

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
                print(f"Course id: {course.get_cid()}" ,
                      f"Course name: {course.get_cname()}", sep="\n")

    # Function to list student marks for a given course
    def list_mark(self):
        cid = int(input("Enter id of course you want to list marks: "))
        while cid <= 0:
            cid = int(input("Course id must be positive.Enter  again course id you want to list marks: "))
        if len(self.marks) == 0:
            print("The mark list is empty!!!")
        else:
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
                "6.List students \n"                  \
                "7.List courses \n"                   \
                "8.List marks \n"                     \
                "9.Exist!!!" ,
                )
        while True:
            select = int(input("Select operations form 1, 2, 3, 4, 5, 6, 7, 8, 9:"))
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
                self.list_students()
            elif select == 7:
                self.list_courses()
            elif select == 8:
                self.list_mark()
            elif select == 9:
                print("Existed!!!")
                break
            else:
                print("Invalid value")
                

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    # Create object driver
    d = Driver()
    d.run_Driver()
