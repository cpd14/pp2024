import os
import gzip

from domains.studentmanagementsystem import StudentManagementSystem

# Check if students.dat exists
def check_data_file():
    if os.path.exists("students.dat"):
        # Decompress and load data from students.dat
        with gzip.open("students.dat", "rb") as input_file:
            data = input_file.read()
            # Handle the decompressed data as needed
            # For example, you can write it back to the respective files
            with open("input.py", "wb") as output_file:
                output_file.write(data)

check_data_file()

if __name__ == '__main__':
    system = StudentManagementSystem()
    system.run()
    
def compress_files():
    files_to_compress = ["input.py", "output.py", "pw4/domains/student.py", "pw4/domains/course.py", "pw4/domains/student_management_system.py", "main.py"]
    with gzip.open("students.dat", "wb") as output_file:
        for file_name in files_to_compress:
            with open(file_name, "rb") as input_file:
                output_file.write(input_file.read())

compress_files()