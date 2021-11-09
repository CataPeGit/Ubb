import repository
from domain.student_list import *
from utils.general_functions import *
from repository.student_repo import StudentRepository

import unittest


# to run unittests type the following command into the terminal/cmd from the root of the project (where the main is)
# python -m unittest discover -s tests -p '*_tests.py'
class TestStudentRepository(unittest.TestCase):
    def test_get_students_with_maximum_average_grade(self):
        """
        Test function get students with maximum average grade
        :return:
        """
        students = StudentRepository([Student('a', 811, [5, 6, 7], 1)])
        self.assertEqual(students.get_students_with_maximum_average_grade(), StudentRepository([Student('a', 811, [5, 6, 7], 1)]))

        students = StudentRepository()
        self.assertEqual(students.get_students_with_maximum_average_grade(), StudentRepository())

        students = StudentRepository([Student('a', 811, [5, 6, 7], 1), Student('b', 811, [1, 6, 7], 2)])
        self.assertEqual(students.get_students_with_maximum_average_grade(), StudentRepository([Student('a', 811, [5, 6, 7], 1)]))

        students = StudentRepository([Student('a', 811, [5, 6, 7], 1), Student('b', 811, [1, 6, 7], 2), Student('c', 812, [6], 3)])
        self.assertEqual(students.get_students_with_maximum_average_grade(), StudentRepository([Student('a', 811, [5, 6, 7], 1), Student('c', 812, [6], 3)]))

    def test_get_students_with_maximum_grade(self):
        """
        Test function get students with maximum grade
        :return:
        """
        students = StudentRepository([Student('a', 811, [5, 6, 7], 1)])
        self.assertEqual(students.get_students_with_maximum_grade(), StudentRepository([Student('a', 811, [5, 6, 7], 1)]))

        students = StudentRepository()
        self.assertEqual(students.get_students_with_maximum_grade(), StudentRepository())

        students = StudentRepository([Student('a', 811, [5, 6, 9], 1), Student('b', 811, [1, 6, 7], 2)])
        self.assertEqual(students.get_students_with_maximum_grade(), StudentRepository([Student('a', 811, [5, 6, 9], 1)]))

        students = StudentRepository([Student('a', 811, [5, 6, 7], 1), Student('b', 811, [1, 6, 7], 2), Student('c', 812, [6], 3)])
        self.assertEqual(students.get_students_with_maximum_grade(), StudentRepository([Student('a', 811, [5, 6, 7], 1), Student('b', 811, [1, 6, 7], 2)]))

    def test_get_student_from_group(self):
        """
        Test function get students from a given group
        :return:
        """
        students = StudentRepository([Student('a', 811, [5, 6, 7], 1)])
        self.assertEqual(students.get_student_from_group(811), StudentRepository([Student('a', 811, [5, 6, 7], 1)]))
        self.assertEqual(students.get_student_from_group(812), StudentRepository())

        students = StudentRepository([Student('a', 811, [5, 6, 7], 1), Student('b', 811, [1, 6, 7], 2), Student('c', 812, [6], 3)])
        self.assertEqual(students.get_student_from_group(811), StudentRepository([Student('a', 811, [5, 6, 7], 1), Student('b', 811, [1, 6, 7], 2)]))

    def test_get_average_grade_of_maximums_from_same_group(self):
        """
        Test function calculating the average of maximum grades from a given group
        :return:
        """
        students = StudentRepository([Student('a', 811, [5, 6, 7], 1)])
        self.assertEqual(students.get_average_grade_of_maximums_from_same_group(811), 7)
        self.assertEqual(students.get_average_grade_of_maximums_from_same_group(812), 0.0)

        students = StudentRepository([Student('a', 811, [5, 6, 7], 1), Student('b', 811, [1, 6, 5], 2), Student('c', 812, [6], 3)])
        self.assertEqual(students.get_average_grade_of_maximums_from_same_group(811), 6.5)

        students = StudentRepository([Student('a', 811, [], 1)])
        self.assertEqual(students.get_average_grade_of_maximums_from_same_group(811), 0.0)

    def test_get_minimum_grade_from_group(self):
        """
        Test function calculating the minimum grades from a given group
        :return:
        """
        students = StudentRepository([Student('a', 811, [5, 6, 7], 1)])
        self.assertEqual(students.get_minimum_grade_from_group(811), 5)
        self.assertRaises(ValueError, students.get_minimum_grade_from_group, 812)

        students = StudentRepository([Student('a', 811, [5, 6, 7], 1), Student('b', 811, [1, 6, 5], 2), Student('c', 812, [6], 3)])
        self.assertEqual(students.get_minimum_grade_from_group(811), 1.0)


def test_add_student():
    """
    Test function add_student
    :return:
    """
    students = StudentRepository()
    students.add_student(["a", 812, [8], 1])
    assert students.get_number_of_students() == 1
    assert students == StudentRepository([Student("a", 812, [8], 1)])
    try:
        students.add_student(["b", 812, [0], 2])
        assert False
    except ValueError:
        assert True
    assert students.get_number_of_students() == 1
    assert students == StudentRepository([Student("a", 812, [8], 1)])

    try:
        students.add_student(["c", 813, [100], 3])
        assert False
    except ValueError:
        assert True
    assert students.get_number_of_students() == 1
    assert students == StudentRepository([Student("a", 812, [8], 1)])


def test_insert_student():
    students = StudentRepository()
    students.insert_student(0, "a", 812, [8], 1)
    assert students == StudentRepository([Student("a", 812, [8], 1)])

    #  |                   |
    # [ , Student("a", 8),  ]
    try:
        students.insert_student(2, "b", 812, [7], 2)
        assert False
    except IndexError:
        assert True

    try:
        students.insert_student(-2, "b", 812, [7], 2)
        assert False
    except IndexError:
        assert True

    try:
        students.insert_student(0, "b", 812, [17], 2)
        assert False
    except ValueError:
        assert True

    students.insert_student(1, "b", 812, [7], 2)
    assert students == StudentRepository([Student("a", 812, [8], 1), Student("b", 812, [7], 2)])


def test_get_number_of_students():
    assert StudentRepository().get_number_of_students() == 0
    assert StudentRepository([Student("a", 812, [8], 1)]).get_number_of_students() == 1
    assert StudentRepository([Student("a", 812, [8], 1), Student("b", 812, [7], 2)]).get_number_of_students() == 2


def test_get_index_of_student_with_id():
    """
    Test function get index of a student from the repository who has the given ID
    """
    assert StudentRepository().get_index_student_with_id(1) == -1

    s = StudentRepository([Student("a", 812, [5], 1), Student("b", 812, [7], 2)])
    assert s.get_index_student_with_id(1) == 0
    assert s.get_index_student_with_id(2) == 1


def test_get_all_students():
    """
    Test function get all students from the repository
    """
    assert StudentRepository().get_all_students() == []

    s = StudentRepository([Student("a", 812, [5], 1), Student("b", 812, [7], 2)])
    assert len(s.get_all_students()) == 2
    assert s.get_all_students() == [Student("a", 812, [5], 1), Student("b", 812, [7], 2)]


def test_get_student_at_index():
    """
    Test function get student from the repository at a given index
    """
    s = StudentRepository([Student("a", 812, [5], 1), Student("b", 812, [7], 2)])
    assert s.get_student_at_index(0) == Student("a", 812, [5], 1)
    assert s.get_student_at_index(1) == Student("b", 812, [7], 2)
    try:
        s.get_student_at_index(2)
        assert False
    except IndexError:
        assert True


def test_get_student_by_id():
    """
    Test function get student from the repository with a given ID
    """
    s = StudentRepository([Student("a", 812, [5], 1), Student("b", 812, [7], 2)])
    assert s.get_student_by_id(1) == Student("a", 812, [5], 1)
    assert s.get_student_by_id(2) == Student("b", 812, [7], 2)
    try:
        s.get_student_by_id(3)
        assert False
    except ValueError:
        assert True


def test_get_students_grade_less():
    """
    Test function get students from the repository with grade less than the given value
    """
    s = StudentRepository([Student("a", 812, [5], 1), Student("b", 812, [7], 2)])
    assert s.get_students_with_value_less(6) == StudentRepository([Student("a", 812, [5], 1)])
    assert s.get_students_with_value_less(10) == StudentRepository([Student("a", 812, [5], 1), Student("b", 812, [7], 2)])


def test_update_student_at_index():
    """
    Test function update student from the repository at a given index
    """
    s = StudentRepository([Student("a", 812, [5], 1), Student("b", 812, [7], 2)])
    s.update_at_index(0, "c", 813, [8])
    assert s.get_student_at_index(0).get_name() == "c"
    assert s.get_student_at_index(0).get_group() == 813
    assert s.get_student_at_index(0).get_grades() == [8]

    try:
        s.update_at_index(-1, "d", 811, [4])
        assert False
    except IndexError:
        assert True

    try:
        s.update_at_index(100, "d", 811, [4])
        assert False
    except IndexError:
        assert True


def test_update_student_by_id():
    """
    Test function update student from the repository with a given ID
    """
    s = StudentRepository([Student("a", 812, [5], 1), Student("b", 812, [7], 2)])
    s.update_by_id(1, "c", 813, [8])
    assert s.get_student_by_id(1).get_name() == "c"
    assert s.get_student_by_id(1).get_group() == 813
    assert s.get_student_by_id(1).get_grades() == [8]

    try:
        s.update_by_id(-1, "d", 811, [4])
        assert False
    except ValueError:
        assert True


def test_delete_student_at_index():
    """
    Test function delete student from the repository at a given index
    """
    s = StudentRepository([Student("a", 812, [5], 1), Student("b", 812, [7], 2)])
    s.delete_at_index(0)
    assert s.get_number_of_students() == 1
    assert s.get_student_at_index(0).get_id() == 2
    assert s.get_student_at_index(0).get_name() == "b"
    assert s.get_student_at_index(0).get_group() == 812
    assert s.get_student_at_index(0).get_grades() == [7]

    try:
        StudentRepository().delete_at_index(0)
        assert False
    except IndexError:
        assert True


def test_delete_student_by_id():
    """
    Test function delete student from the repository with a given ID
    """
    s = StudentRepository([Student("a", 812, [5], 1), Student("b", 812, [7], 2)])
    s.delete_by_id(1)
    assert s.get_number_of_students() == 1
    assert s.get_student_at_index(0).get_name() == "b"
    assert s.get_student_at_index(0).get_group() == 812
    assert s.get_student_at_index(0).get_grades() == [7]

    try:
        s.delete_by_id(-1)
        assert False
    except ValueError:
        assert True


def all_tests():
    """
    Run all tests.
    :return:
    """
    test_add_student()
    test_insert_student()
    test_get_number_of_students()
    test_get_index_of_student_with_id()
    test_get_all_students()
    test_get_student_at_index()
    test_get_student_by_id()
    test_get_students_grade_less()
    test_update_student_at_index()
    test_update_student_by_id()
    test_delete_student_at_index()
    test_delete_student_by_id()
