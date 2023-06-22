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

        switch_case = {
            '1': student.add_student,
            '2': student.read_students,
            '3': student.update_student,
            '4': student.delete_student,
            '5': student.search_student,
            '6': lambda: None  # Placeholder for "Back" option
        }

        # Execute the selected function based on choice
        selected_function = switch_case.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Invalid choice. Please try again.\n")

        if choice == "6":
            break


def option_course():
    while True:
        print("1. Add Course")
        print("2. Course list")
        print("3. Edit course")
        print("4. Delete course")
        print("5. Search")
        print("6. Back")
        choice = input("Enter your choice: ")

        switch_case = {
            '1': course.add_course,
            '2': course.read_course,
            '3': course.update_course,
            '4': course.delete_course,
            '5': course.search_course,
            '6': lambda: None  # Placeholder for "Back" option
        }

        # Execute the selected function based on choice
        selected_function = switch_case.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Invalid choice. Please try again.\n")

        if choice == "6":
            break


if __name__ == "__main__":
    while True:
        print("1. Options for Courses")
        print("2. Options for Students")
        print("3. Exit")
        choice = input("Enter your choice: ")
        print()

        switch_case = {
            '1': option_course,
            '2': option_student,
            '3': lambda: None  # Placeholder for "Exit" option
        }

        # Execute the selected function based on choice
        selected_function = switch_case.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Invalid choice. Please try again.\n")

        if choice == "3":
            break
