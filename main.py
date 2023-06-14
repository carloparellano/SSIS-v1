import student
import course

def option_student():
    while True:
        print("Good Day! Welcome")
        print("1. Add student")
        print("2. Student list")
        print("3. Edit student")
        print("4. Delete student")
        print("5. Search")
        print("6. Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            student.add_student()

        elif choice == "2":
            student.read_students()

        elif choice == "3":
            student.update_student()

        elif choice == "4":
            student.delete_student()

        elif choice == "5":
            student.search_student()

        elif choice == "6":
            break

        else:
            print("Invalid Choice. Please try again.\n")


def option_course():
    while True:
        print("1. Add Course")
        print("2. Course list")
        print("3. Edit course")
        print("4. Delete course")
        print("5. Search")
        print("6. Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            course.add_course()

        elif choice == "2":
            course.read_course()

        elif choice == "3":
            course.update_course()

        elif choice == "4":
            course.delete_course()

        elif choice == "5":
            course.search_course()

        elif choice == "6":
            break

        else:
            print("Invalid Choice. Please try again.\n")


if __name__ == "__main__":
    while True:
        print("1. CRUDL For Students")
        print("2. CRUDL For Courses")
        print("3. Exit")
        choice1 = input("Enter your choice: ")
        print()
        if choice1 == '1':
            option_student()
        elif choice1 == '2':
            option_course()
        elif choice1 == '3':
            break
        else:
            print("Invalid Choice. Please try again.\n")