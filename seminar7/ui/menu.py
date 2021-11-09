from repository.student_repo import StudentRepository
from domain.student_list import Student


def print_menu():
    """
    Print the menu options available in the interface.
    :return:
    """
    print("0 - exit program")
    print("1 - print menu")
    print("2 - print students")
    print("3 - add new student")
    print("4 - insert student")
    print("5 - get number of students")


def start():
    """
    Start the menu type console.
    :return:
    """
    print_menu()
    command = input(">>> ")
    # [["name1", grade1], ["name2", grade2], ...]
    # from now on
    # [Student(name1, grade1), Student(name2, grade2), ...)
    student_list = StudentRepository([
        Student("a", 8),
        Student("b", 10),
        Student("c", 4)
    ])
    while command != "0":
        if command == "1":
            print_menu()
        elif command == "2":
            print(student_list)
        elif command == "3":
            new_entry = []
            try:
                new_entry.append(input("New id: "))
                new_entry.append(input("New name: "))
                new_entry.append(int(input("New grade: ")))
                student_list.add_student(new_entry)
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
            else:
                print(student_list)
        elif command == "4":
            student_id = input("ID of the student: ")
            read_name = input("Student name: ")
            try:
                grade = int(input("Grade of the student: "))
                index = int(input("Index of the new student: "))
            except ValueError:
                print("Grade and index should be numbers!")
            else:
                try:
                    student_list.insert_student(index, student_id, read_name, grade)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)
                else:
                    print(student_list)
        elif command == "5":
            print(f"Number of students in the repository: {student_list.get_number_of_students()}")
        else:
            print("Invalid command")
        command = input(">>> ")
