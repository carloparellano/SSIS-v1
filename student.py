class Student:
    def __init__(self, name, id, year_level, course):
        self.name = name
        self.id = id
        self.year_level = year_level
        self.course = course

students = []

# create text file and close it
file = open("students.txt", "w")
file.close()

def add_student():
    name = input("Enter student name: ")
    id = input("Enter student ID: ")
    year_level = input("Enter student year level: ")
    course = input("Enter student course: ")
    student = Student(name, id, year_level, course)
    students.append(student)
    print("Student added successfully.")
    
    # add new student to text file
    file = open("students.txt", "a")
    file.write(f"{name}  |  {id}  |  {year_level}  |  {course}\n")
    file.close()

def read_students():
    file = open("students.txt", "r")
    for line in file:
        data = line.strip().split("|")
        name, id, year_level, course = data
        print(f"Student Name: {name}  ---  Student ID: {id}  ---  Student Year Level: {year_level}  ---  Student Course: {course}")
    file.close()

def update_student(): 
    id = input("Enter student ID to update: ")
    for student in students:
        if student.id == id:
            student.name = input("Enter new name: ")
            student.year_level = input("Enter new year level: ")
            student.course = input("Enter new course: ")
            print("Student updated successfully.")
        
            file = open("students.txt", "w")
            for s in students:
                file.write(f"{s.name}|{s.id}|{s.year_level}|{s.course}\n")
            file.close()
            return
    print("Student not found.")

def delete_student():
    id = input("Enter student ID to delete: ")
    for i, student in enumerate(students):
        if student.id == id:
            del students[i]
            print("Student deleted successfully.")
            
            file = open("students.txt", "w")
            for s in students:
                file.write(f"{s.name}|{s.id}|{s.year_level}|{s.course}\n")
            file.close()
            return
    print("Student not found.")
    
def search_student():
    search_term = input("Enter search term: ")
    found = False
    for student in students:
        if search_term.lower() in student.name.lower() or search_term.lower() in student.course.lower() or search_term == student.id:
            print(f"Student Name: {student.name}\n Student ID: {student.id}\n Student Year Level: {student.year_level}\n Student Course: {student.course}\n")
            found = True
    if not found:
        print("No matching results found.")

while True:
    print("Good Day! Welcome!")
    print("1. Add student")
    print("2. Student list")
    print("3. Edit student")
    print("4. Delete student")
    print("5. Search")
    print("6. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        read_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()
        
    elif choice == "5":
        search_student()
        
    elif choice == "6":
        break
    
    else: 
        print("Invalid Choice. Please try again.")
