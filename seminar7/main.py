from ui.menu import start
from tests.run import all_tests


all_tests()
# you can also move this print to the end of functions all_tests
print("All tests passed!\n")
start()


# from domain.student_list import Student
# try:
#     s = Student("a", 4)
# except ValueError as ve:
#     print(ve)
# else:
#     print(s)

# from repository.student_repo import StudentRepository
#
# repo = StudentRepository([Student("a", 8)])
# print(repo)
# print(StudentRepository())
