import math
from domains.Student import *
from domains.Course import *
from domains.Mark import *

sf = open("students.txt", "w")
cf = open("courses.txt", "w")
mf = open("marks.txt", "w")


# Function to input datas from .txt file
def input_mark_file(driver, sid, sname, sdob, cid, cname, credit, value):
    # Set for students
    s_sid = driver.mark.student.set_sid(sid) #int
    s_sname = driver.mark.student.set_sname(sname) #str
    s_sdob = driver.mark.student.set_sdob(sdob) #str
    student = Student(s_sid, s_sname, s_sdob)

    # Set for courses
    s_cid = driver.mark.course.set_cid(cid) #int
    s_cname = driver.mark.course.set_cname(cname) #str
    s_credit = driver.mark.course.set_credit(credit)   #int
    course = Course(s_cid, s_cname, s_credit)
    # Set for marks
    s_value = driver.mark.set_value(value) #int
    
    driver.marks.append(Mark(driver, student, course, s_value))

def input_students_file(driver, sid, sname, sdob):
    student = Student(driver, sid, sname, sdob)
    driver.students.append(student)

def input_courses_file(driver, cid, cname, credit):
    course = Course(driver, cid, cname, credit)
    driver.courses.append(course)


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
    def input_students_infor(self, driver):
        if  self.driver.nofstudents == None or self.driver.nofstudents <= 0:
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

                self.driver.students.append(Student(driver, sid, sname, sdob))

                #Writing data to file students.txt 
                sf = open("students.txt", "a")
                sf.write(str(sid))
                sf.write("\n")
                sf.write(sname)
                sf.write("\n")
                sf.write(sdob)
                sf.write("\n")
                sf.close()
        else:
            print(
                f"The student list is full({len(self.driver.students)} students).Please use function 1 to extra student list")


    # Function to input information of courses
    def input_courses_infor(self, driver):
        if self.driver.nofcourses == None or self.driver.nofcourses <= 0:
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
                self.driver.courses.append(Course(driver, cid, cname, credit))


                #Writing data to file courses.txt 
                cf = open("courses.txt", "a")
                cf.write(str(cid))
                cf.write("\n")
                cf.write(cname)
                cf.write("\n")
                cf.write(str(credit))
                cf.write("\n")
                cf.close()

        else:
            print(
                f"The list of courses is full({len(self.driver.courses)} courses).Please use function 2 to extra student list")

    # Function to input mark of exactly courses for students
    def input_mark(self, driver):
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

                        self.driver.marks.append(Mark(driver, student, course, value))

                        #Writing data to file courses.txt 
                        mf = open("marks.txt", "a")
                        #Student
                        mf.write(str(student.get_sid()))
                        mf.write("\n")
                        mf.write(student.get_sname())
                        mf.write("\n")
                        mf.write(student.get_sdob())
                        mf.write("\n")
                        #Course
                        mf.write(str(course.get_cid()))
                        mf.write("\n")
                        mf.write(str(course.get_cname()))
                        mf.write("\n")
                        mf.write(str(course.get_credit()))
                        mf.write("\n")
                        #Mark
                        mf.write(str(value))
                        mf.write("\n")
                        mf.close()
        else:
            print("Course id is not existed!!!")
