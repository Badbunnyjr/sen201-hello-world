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
        print(student)

# Example usage
add_student("John Doe", "SEN201001", "Computer Science", "200")
view_students()
