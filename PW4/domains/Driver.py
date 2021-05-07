from PW4.input import *
from PW4.output import *


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

    
    # Function to run the program
    def run_Driver(self, inputt, output):
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
                inputt.input_number_students()    
            elif select == 2:
                inputt.input_number_courses()
            elif select == 3:
                inputt.input_students_infor()
            elif select == 4:
                inputt.input_courses_infor()
            elif select == 5:
                inputt.input_mark()
            elif select == 6:
                output.calculate_GPA()
            elif select == 7:
                output.self.sort_student_list()
            elif select == 8:
                output.list_students()
            elif select == 9:
                output.list_courses()
            elif select == 10:
                output.list_mark()
            elif select == 11:
                print("Existed!!!")
                break
            else:
                print("Invalid value")
                
