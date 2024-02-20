class Entity:
    def __init__(self, identifier, name, date_of_birth):
        self.id = identifier
        self.name = name
        self.dob = date_of_birth

    def __str__(self):
        return f"{self.id}, {self.name}, {self.dob}"

class Course(Entity):
    def __init__(self, identifier, name, marks):
        super().__init__(identifier, name, None)
        self.marks = marks

    def list_marks(self):
        print(f"\nStudent Marks for {self.name}:")
        for student_id, mark in self.marks.items():
            student = next((student for student in students if student.id == student_id), None)
            print(f"Student ID: {student_id}, Name: {student.name}, DoB: {student.dob}, Marks: {mark}")

class Student(Entity):
    def __init__(self, identifier, name, date_of_birth):
        super().__init__(identifier, name, date_of_birth)

class Input:
    @staticmethod
    def entity(entity_name):
        return tuple(input(f"Enter {entity_name} ID, name, and date of birth (comma-separated): ").split(', '))

    @staticmethod
    def marks(students, selected_course):
        return {student.id: input(f"Enter marks for {student.name} in {selected_course.name}: ") for student in students}

class List:
    @staticmethod
    def entities(entities, entity_name):
        print(f"\nList of {entity_name}s:")
        for entity in entities:
            print(f"{entity_name} ID: {entity.id}, Name: {entity.name}")

class Main:
    def __init__(self):
        self.num_students = int(input("Enter the number of students: "))
        self.students = [Student(*Input.entity("Student")) for _ in range(self.num_students)]

        self.num_courses = int(input("Enter the number of courses: "))
        self.courses = [Course(*Input.entity("Course"), {}) for _ in range(self.num_courses)]

        selected_course_id = input("Enter the course ID for marks: ")
        self.selected_course = next((course for course in self.courses if course.id == selected_course_id), None)

        if self.selected_course:
            self.marks = Input.marks(self.students, self.selected_course)
            self.selected_course.marks = self.marks

            List.entities(self.courses, "Course")
            List.entities(self.students, "Student")
            self.selected_course.list_marks()
        else:
            print("Invalid course ID. Please select a valid course.")

if __name__ == "__main__":
    Main()
