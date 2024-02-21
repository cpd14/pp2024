class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob
        self.student_courses = {}

    def input_marks(self, course_id, mark):
        self.student_courses[course_id] = mark

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Date of Birth: {self.student_dob}")

    def display_marks(self):
        for course_id, mark in self.student_courses.items():
            print(f"Course ID: {course_id}, Mark: {mark}")


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student date of birth: ")
            student = Student(student_id, student_name, student_dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_marks(self):
        course_id = input("Enter the course ID to input marks: ")
        mark = float(input("Enter the mark: "))

        for student in self.students:
            student_id = student.student_id
            student.input_marks(course_id, mark)
            print(f"Mark {mark} for student {student_id} in course {course_id} has been recorded.")

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            student.display_info()

    def show_marks(self):
        course_id = input("Enter the course ID to show marks: ")
        print(f"Student marks for course {course_id}:")
        for student in self.students:
            student_id = student.student_id
            student_name = student.student_name
            if course_id in student.student_courses:
                mark = student.student_courses[course_id]
                print(f"Student ID: {student_id}, Student Name: {student_name}, Mark: {mark}")

    def run(self):
        self.input_students()
        self.input_courses()

        while True:
            print("\nSelect an option:")
            print("1. Input marks")
            print("2. List courses")
            print("3. List students")
            print("4. Show student marks for a course")
            print("0. Exit")

            option = input("Enter your choice: ")

            if option == "1":
                self.input_marks()
            elif option == "2":
                self.list_courses()
            elif option == "3":
                self.list_students()
            elif option == "4":
                self.show_marks()
            elif option == "0":
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == '__main__':
    system = StudentManagementSystem()
    system.run()