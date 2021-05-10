import numpy as np


class Output:
    def __init__(self, driver):
        self.driver = driver

    # Function to calculate GPA for given student
    def calculate_GPA(self):
        while True:
            try:
                sid = int(input(f"Enter student id you want to calculate GPA: "))
                while sid <= 0:
                    sid = int(input(f"ID must be positive. Enter again student id: "))

                # check = 0
                # for mark in self.driver.marks:
                #     if check == (len(self.driver.marks) - 1):
                #         print(f"Error. Student id {sid} not existed!!!")
                #         break
                #     elif sid != mark.get_student().get_sid():
                #         check = check + 1
                #     else:
                #         print("Student id is existed!!!")
                exist = 0
                for student in self.driver.students:
                    if student.get_sid() == sid:
                        exist = 1
                if exist == 0:
                    print(f"Error. Student id {sid} not existed!!!")
                elif exist == 1:
                    break
            except:
                print("ID must be positive. Enter again student id!!!")
            else:
                break

        list_score = np.array([])
        list_credit = np.array([])

        check = 0
        for mark in self.driver.marks:
            if sid == mark.get_student().get_sid():
                list_score = np.append(list_score, mark.get_value())
                list_credit = np.append(list_credit, mark.get_course().get_credit())

        gpa = np.dot(list_score, list_credit) / np.sum(list_credit)

        for student in self.driver.students:
            if sid == student.get_sid():
                student.set_gpa(gpa)

    # Function to sort student list by GPA decrending
    def sort_student_list(self):
        if len(self.driver.students) == 0:
            print("List of student information is empty!!!")
        else:
            data_type = [('sid', 'S30'), ('sname', 'S30'), ('gpa', float)]
            new_students = []
            for student in self.driver.students:
                new_student_infor = (student.get_sid(), student.get_sname(), student.get_gpa())
                new_students.append(new_student_infor)
            sorting_new_students = np.array(new_students, dtype=data_type)
            sorted_list = np.sort(sorting_new_students, order='gpa')
            print(sorted_list)

    #### Display functions (3)

    # Function to list all student's informations
    def list_students(self):
        if len(self.driver.students) == 0:
            print("The student list is empty!!!")
        else:
            print("Student id", "Student name", "Student dob", sep="             ")
            for student in self.driver.students:
                print(f"{student.get_sid()}",
                      f"{student.get_sname()}",
                      f"{student.get_sdob()}", sep="             ")

    # Function to list all course's informations
    def list_courses(self):
        if len(self.driver.courses) == 0:
            print("The course list is empty!!!")
        else:
            for course in self.driver.courses:
                print(f"Course id: {course.get_cid()}\n"
                      f"Course name: {course.get_cname()}\n", sep=" - ")

    # Function to list student marks for a given course
    def list_mark(self):
        if len(self.driver.marks) == 0:
            print("The mark list is empty!!!")
        else:
            while True:
                try:
                    cid = int(input("Enter id of course you want to list marks: "))
                    while cid <= 0:
                        cid = int(input("Course id must be positive.Enter  again course id you want to list marks: "))

                    check = 0
                    for mark in self.driver.marks:
                        if check == (len(self.driver.marks) - 1):
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
            for mark in self.driver.marks:
                if cid == mark.get_course().get_cid():
                    print(mark.get_student().get_sname(), mark.get_course().get_cname(), mark.get_value(), sep="-")
