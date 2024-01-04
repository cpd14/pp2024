def input_students():
    num_students = int(input("Enter the number of students: "))
    students = []
    for _ in range(num_students):
        student_id = input("Enter student id: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        student_courses = {}
        student_info = (student_id, student_name, student_dob, student_courses)
        students.append(student_info)
    return students

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = {}
    for _ in range(num_courses):
        course_id = input("Enter course id: ")
        course_name = input("Enter course name: ")
        courses[course_id] = course_name
    return courses

def input_marks(students, courses):
    course_id = input("Enter the course id to input marks: ")
    for student_info in students:
        student_id = student_info[0]
        mark = float(input(f"Enter the mark for student {student_id} in course {course_id}: "))
        student_info[3][course_id] = mark

def list_courses(courses):
    print("List of courses:")
    for course_id, course_name in courses.items():
        print(f"Course id: {course_id}, Course name: {course_name}")

def list_students(students):
    print("List of students:")
    for student_info in students:
        student_id, student_name, student_dob, _ = student_info
        print(f"Student id: {student_id}, Student name: {student_name}, Date of birth: {student_dob}")

def show_marks(students):
    course_id = input("Enter the course id to show marks: ")
    print(f"Student marks for course {course_id}:")
    for student_info in students:
        student_id, student_name, _, student_courses = student_info
        if course_id in student_courses:
            mark = student_courses[course_id]
            print(f"Student id: {student_id}, Student name: {student_name}, Mark: {mark}")

def main():
    students = input_students()
    courses = input_courses()

    while True:
        print("\nSelect an option:")
        print("1. Input marks")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("0. Exit")
        
        option = input("Enter your choice: ")
        
        if option == "1":
            input_marks(students, courses)
        elif option == "2":
            list_courses(courses)
        elif option == "3":
            list_students(students)
        elif option == "4":
            show_marks(students)
        elif option == "0":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()