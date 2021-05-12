import Input
import Output
import os
import pickle

class Driver:
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

    def __init__(self):
        self.input = Input.Input(self)
        self.output = Output.Output(self)

    # Function to run the program
    def run_Driver(self):
        #Upon starting the program
        if os.path.isfile('students.dat'):  # Check if students.dat exist
            # Load number of students and number of courses
            students_file1 = open('students.dat', 'rb')
            self.nofstudents = pickle.load(students_file1)
            self.nofcourses = pickle.load(students_file1)

            # Load information of students
            list_students = pickle.load(students_file1)
            i = 1
            for student in list_students:
                if i <= len(self.nofstudents):
                    self.students.append(student)
                    i = i + 1
                else:
                    break
            #Load information of courses
            list_students2 = pickle.load(students_file1)
            j = 1
            for course in list_students2:
                if i <= len(self.nofcourses):
                    self.courses.append(course)
                    j = j + 1
                else:
                    break

            #Load information of marks
            list_students3 = pickle.load(students_file1)
            for mark in list_students3:
                self.marks.append(mark)

            students_file1.close()

        print("Please select operation: \n"
              "1.Input number of students \n"
              "2.Input number of courses \n"
              "3.Input information for students \n"
              "4.Input information for courses \n"
              "5.Input mark for given courses \n"
              "6.Calculate GPA for given student\n"
              "7.Sort student by gpa\n"
              "8.List students \n"
              "9.List courses \n"
              "10.List marks \n"
              "11.Exit")
        while True:
            select = int(input("Select operations form 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11:"))
            if select == 1:
                self.input.input_number_students()
            elif select == 2:
                self.input.input_number_courses()
            elif select == 3:
                self.input.input_students_infor(self)
            elif select == 4:
                self.input.input_courses_infor(self)
            elif select == 5:
                self.input.input_mark(self)
            elif select == 6:
                self.output.calculate_GPA()
            elif select == 7:
                self.output.sort_student_list()
            elif select == 8:
                self.output.list_students()
            elif select == 9:
                self.output.list_courses()
            elif select == 10:
                self.output.list_mark()
            elif select == 11:
                print("Exited!!!")
                break
            else:
                print("Invalid value")
