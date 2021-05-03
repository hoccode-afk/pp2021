#! usr/bin/python3

class Student:
    def __init__(self, main, sid, sname, sdob):
        self.sid = id
        self.sname = sname
        self.sdob = sdob
        Main.students.append(self)
        Main.students_id.append(self.sid)

    def get_sid(self):
        return self.sid
    def get_sname(self):
        return self.sname
    def get_sdob(self):
        return self.sdob


class Course:
    def __init__(self, main, cid, cname):
        self.cid = id
        self.cname = cname
        Main.courses.append(self)
        Main.courses_id.append(self.cid)

    def get_cid(self):
        return self.cid
    def get_cname(self):
        return self.cname

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
            Student(self, sid, sname, sdob)

    #Input course informations:
    def input_course_infor(self):
        for i in range(0, self.nofcourse):
            print(f"Enter information of course {i+1}")
            cid = int(input("Enter course id: "))
            cname = input(f"Enter name of course {cid}: ")
            Course(self, cid, cname)

    #Input mark for student:
    def input_course_mark(self):
        cid = int(input("Enter the course id you want input mark: "))
        for student in self.students:
            sid = student.get_sid()
            value = float(input(f"Enter mark for {student.get_sname()}: "))
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
        print("List all the mark: ")
        for mark in self.marks:
            if mark.get_cid() == cid:
                sid = mark.get_sid()
                for student in self.students:
                    if student.get_sid() == sid:
                        print(f"Student id : {student.get_sid()} \t Student name : {student.get_sname()} \t Mark : {mark.get_value()}")


    def run_main(self):
        m.input_number_course()
        m.input_number_student()
        m.input_student_infor()
        m.input_course_infor()
        m.input_course_mark()
        m.list_courses()
        m.list_students()
        m.list_marks()


if __name__ == '__main__':
    m = Main()
    m.run_main()