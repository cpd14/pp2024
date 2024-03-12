def display_gpa(student):
    print(f"Student ID: {student.student_id}")
    print(f"Student Name: {student.student_name}")
    print(f"Date of Birth: {student.student_dob}")
    print(f"Average GPA: {student.average_gpa:.2f}")

def display_info(student):
    print(f"Student ID: {student.student_id}")
    print(f"Student Name: {student.student_name}")
    print(f"Date of Birth: {student.student_dob}")

def display_marks(student):
    print(f"Student marks for ID {student.student_id}:")
    for course_id, mark in student.student_courses.items():
        print(f"Course ID: {course_id}, Mark: {mark}")