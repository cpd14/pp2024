import numpy as np 
import math

class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob
        self.student_courses = {}
        self.average_gpa = 0.0

    def calculate_gpa(self, courses):
        marks = np.array([self.student_courses.get(course_id, 0.0) for course_id in courses.keys()])
        credits = np.array(list(courses.values()))
        weighted_sum = np.sum(marks * credits)
        total_credits = np.sum(credits)

        if total_credits > 0:
            self.average_gpa = weighted_sum / total_credits
        
