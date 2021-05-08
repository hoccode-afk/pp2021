import math
from domains.Student import *
from domains.Course import *
from domains.Mark import *


class Input:
    def __init__(self, driver):
        self.driver = driver

    # Function to input number of students
    def input_number_students(self):
        while True:
            try:
                self.driver.nofstudents = int(input("Enter number of students: "))
                while self.driver.nofstudents <= 0:
                    print("Number of students has to be positive integer!!!\n")
                    self.driver.nofstudents = int(input("Enter again number of students: "))
            except:
                print("Number of students has to be positive integer!!!\n")
            else:
                break

    # Function to input number of courses
    def input_number_courses(self):
        while True:
            try:
                self.driver.nofcourses = int(input("Enter number of courses: "))
                while self.driver.nofcourses <= 0:
                    print("Number of couses has to be positive integer!!!\n")
                    self.driver.nofcourses = int(input("Enter again number of courses: "))
            except:
                print("Number of courses has to be positive integer!!!\n")
            else:
                break

    # Function to input information of students
    def input_students_infor(self):
        if self.driver.nofstudents <= 0:
            print("Student list is empty. Please enter number of students!!!")
        elif self.driver.nofstudents > len(self.driver.students):
            for i in range(0, self.driver.nofstudents):
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
                        break  # Still not good!!!Name is still entered by numbers

                while True:
                    try:
                        sdob = input(f"Enter date of birth of student #{sid}: ")
                        while len(sdob) == 0:
                            sdob = input(f"Student name can't be empty.Enter agian name of student #{sid}: ")
                    except:
                        print("Student name can't be empty.Enter again name of student!!!")
                    else:
                        break  # Still not good!!!Dob is still entered by letters

                self.driver.students.append(Student(sid, sname, sdob))
        else:
            print(
                f"The student list is full({len(self.driver.students)} students).Please use function 1 to extra student list")

    # Function to input information of courses
    def input_courses_infor(self):
        if self.driver.nofcourses <= 0:
            print("Course list is empty. Please enter number of courses!!!")
        elif self.driver.nofcourses > len(self.driver.courses):
            for i in range(0, self.driver.nofcourses):
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
                self.driver.courses.append(Course(cid, cname, credit))
        else:
            print(
                f"The list of courses is full({len(self.driver.courses)} courses).Please use function 2 to extra student list")

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
        exist = 0
        for course in self.driver.courses:
            if course.get_cid() == cid:
                exist = 1
        if exist == 1:
            for course in self.driver.courses:
                if course.get_cid() == cid:
                    for student in self.driver.students:
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
                        # Round-down student scores to 1-digit decimal
                        value = math.floor(value * 10) / 10.0

                        self.driver.marks.append(Mark(student, course, value))
        else:
            print("Course id is not existed!!!")
