# input.py
import numpy as np
import math
from decimal import Decimal, ROUND_DOWN

def round_mark(mark):
    final_mark = math.floor(mark * 10) / 10
    return final_mark

def input_marks(student):
    num_courses = int(input(f"Enter the number of courses for student {student.student_id}: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        mark = float(input(f"Enter the mark for course {course_id}: "))
        rounded_mark = round_mark(mark)
        student.student_courses[course_id] = rounded_mark
        print(f"Final Mark {rounded_mark} for student {student.student_id} in course {course_id} has been recorded.")

