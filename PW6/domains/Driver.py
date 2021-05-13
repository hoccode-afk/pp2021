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
    # List to store all datas to compress to .dat file
    studentmark = []

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
            # Open and read students.dat - binary access mode
            students_file1 = open('students.dat', 'rb')
            studentmark_list = pickle.load(students_file1)
            if len(studentmark_list) >= 2:
                # Load information of students
                # Load number of students and number of courses
                # Have to input nofstudent and nofcourse at same time
                self.nofstudents = studentmark_list[0] 
                self.nofcourses = studentmark_list[1]

            # Load information of students
            if len(studentmark_list) >= (self.nofstudents + 2):
                for i in range(self.nofstudents): 
                    self.students.append(studentmark_list[i+2])
        
            #Load information of courses
            if len(studentmark_list) >= (self.nofcourses + self.nofstudents + 2):
                for i in range(self.nofcourses): 
                    self.courses.append(studentmark_list[i + 2 + self.nofstudents])

            #Load information of marks
            if (len(studentmark_list) - self.nofstudents - self.nofcourses - 2) > 0: 
                for i in range(len(studentmark_list) - self.nofstudents - self.nofcourses - 2):
                    self.marks.append(studentmark_list[i + 2 + self.nofstudents + self.nofcourses])

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
                file = open('students.dat', 'wb')
                pickle.dump(self.studentmark, file)
                file.close()
                print("Exited!!!")
                break
            else:
                print("Invalid value")
