from asyncio import create_subprocess_exec


class Course:
    def __init__ (self, course_name, college):
        self.course_name = course_name
        self.college = college
        
        
courses = []

file = open("courses.txt", "w")
file.close()

def add_course():
    course_name = input("Enter Course Name: ")
    college = input("Enter College: ")
    course = Course(course_name, college)
    courses.append(course)
    print("Course Successfully Added.")
    
    file = open("courses.txt", "a")
    file.write(f"{course_name} | {college}\n")
    file.close()
    
def read_course():
    file = open("courses.txt", "r")
    for line in file:
        data = line.strip().split("|")
        course_name, college = data
        print(f"Course: {course_name}  |   College: {college}\n")
    file.close()
    
def update_course():
    course_name = input("Enter Course to Edit: ")
    for course in courses:
        if course.course_name == course_name:
            course.course_name = input("Enter Course: ")
            course.college = input("Enter College: ")
            print("Course Updated Successfully")
            
            file = open("courses.txt", "w")
            for c in courses:
                file.write(f"{c.course_name} | {c.college}\n")
            file.close()
            return
    print("Course not found.")     

def delete_course():
    course_name = input("Enter Course to Delete: ")
    for course in courses:
        if course.course_name == course_name:
            courses.remove(course)
            print("Course Successfully Deleted.")
            
            file = open("courses.txt", "w")
            for c in courses:
                file.write(f"{c.course_name} | {c.college}\n")
            file.close()
            return
    print("Course not found.") 

def search_course():
    search_term = input("Enter search term: ")
    found = False
    for course in courses:
        if search_term.lower() in course.course_name.lower() or search_term.lower() in course.college.lower():
            print(f"Course: {course.course_name} | College: {course.college}")
            found = True
    if not found:
        print("No matching result found.")
            
while True:
    print("1. Add Course")
    print("2. Course list")
    print("3. Edit course")
    print("4. Delete course")
    print("5. Search")
    print("6. Quit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_course()

    elif choice == "2":
        read_course()

    elif choice == "3":
        update_course()

    elif choice == "4":
        delete_course()
        
    elif choice == "5":
        search_course()
        
    elif choice == "6":
        break
    
    else: 
        print("Invalid Choice. Please try again.")
