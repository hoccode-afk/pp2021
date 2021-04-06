#! usr/bin/python3

students = []
students_name = []
courses = []
courses_id = []
marks = []

def input_number_student():
    nofstudent = int(input("Enter number of students: "))
    return nofstudent

def input_number_course():
    nofcourse = int(input("Enter number of courses: "))
    return nofcourse


number_of_student = input_number_student()
number_of_course = input_number_course()


def input_student_infor():
    for i in range(1, number_of_student+1):
        sid = input(f"Enter student #{i} id: ")
        sname = input(f"Enter student #{i} name: ")
        sdob = input(f"Enter student #{i} date of birth: ")
        student = [sid, sname, sdob]
        students.append(student)
        students_name.append(sname)

def input_course_infor():
    for i in range(1, number_of_course+1):
        print(f"Enter information of course #{i}:")
        cid = int(input("Enter course id: "))
        cname = input("Enter course name: ")
        course = [cid, cname]
        courses.append(course)
        courses_id.append(cid)

def input_mark():
    cid = int(input("Enter course id you want to input mark: "))
    
    if cid in courses_id:
        for i in range(0, number_of_student):
            input_mark = input(f"Enter mark of course {cid} for student {students_name[i]} :")
            mark_input = [cid, students_name[i], input_mark]
            marks.append(mark_input)

def list_coures():
    for i in range(courses):
        print(f"Course information {i}: ")
        print(courses[i])

def list_students():
    for i in range(students):
        print(f"Student information {i}: ")
        print(students[i])

def output_mark():
    kk = int(input("Enter course id you want to display: "))
    if kk in courses_id:
        for each_item in marks:
            for nested_item in each_item:
                if nested_item == kk:
                    print(each_item)

input_student_infor()
input_course_infor()
input_mark()
output_mark()




