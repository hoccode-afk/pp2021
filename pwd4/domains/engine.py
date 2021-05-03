#! usr/bin/python3

import Input

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
