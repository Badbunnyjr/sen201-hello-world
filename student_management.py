# Student Management System (SMS)
# Name: Egwuchukwu Chibuke
# Matric Number: 23/12877
# Course: SEN201
# Level: 300

# List to store student records
students = []

# Function to add a student
def add_student(name, matric_number, course, level):
    student = {
        "name": name,
        "matric_number": matric_number,
        "course": course,
        "level": level
    }
    students.append(student)

# Function to view all students
def view_students():
    for student in students:
        print("Name:", student["name"])
        print("Matric Number:", student["matric_number"])
        print("Course:", student["course"])
        print("Level:", student["level"])
        print("---------------------------")

# Example usage (Your details)
add_student("Egwuchukwu Chibuke", "23/12877", "SEN201", "300")
view_students()
