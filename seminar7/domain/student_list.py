import random


class Student:
    def __init__(self, name, group, grades, student_id=None):
        if student_id is None:
            self.__id = random.randint(1, 1000)
        else:
            self.__id = student_id
        self.__name = name
        for grade in grades:
            if not 0 < grade < 11:
                raise ValueError(f"The grade should be between 1 and 10, but {grade} got.")
        self.__grades = grades
        self.__group = group

    def __eq__(self, other):
        """
        Check if the parameter is equal to the current object.
        :param other: another Student object
        :return: boolean: true if the attributes of the two object are equal, false otherwise
        """
        grades_equal = True
        if len(self.__grades) != len(other.__grades):
            grades_equal = False
        else:
            for i in range(len(self.__grades)):
                if self.__grades[i] != other.__grades[i]:
                    grades_equal = False
                # equal = equal & self.grades[i] != other.grades[i]
        return self.__name == other.__name and self.__group == other.__group and \
               self.__id == other.__id and grades_equal

    def __str__(self):
        """
        Converting a Student object into a string.
        :return:
        """
        return f"{self.__id} {self.__name} ({self.__group}) has grades {self.__grades}"

    # we don't need a setter for the ID we don't want to change it after creating the object

    def get_id(self):
        """
        Get the ID of the student
        :return: id of the student
        """
        return self.__id

    def get_name(self):
        """
        Get the name of the student
        :return: name of the student
        """
        return self.__name

    def set_name(self, new_name):
        """
        Set a new name to the student.
        :param new_name: new name of the student
        """
        self.__name = new_name

    def get_group(self):
        """
        Get group of the student
        :return: group of the student
        """
        return self.__group

    def set_group(self, new_group):
        """
        Set a new group to the student
        :param new_group: new group of the student
        """
        self.__group = new_group

    def get_grades(self):
        """
        Get grades of the student.
        :return: list of grades of the student
        """
        return self.__grades

    def set_grades(self, grades):
        """
        Set new grade list to the student
        :param grades: new list of grades
        """
        for i in range(len(grades)):
            if grades[i] > 11 or grades[i] < 0:
                raise ValueError(f"Grade should be between 1 and 10, but {grades[i]} got.")
        self.__grades = grades.copy()

    def has_grades(self):
        """
        Checks if the student has any grades or not
        :return: True if the student has at least one grade, False otherwise
        """
        return len(self.__grades) > 0

    def average_grade(self):
        """
        Calculate average grade of the student.
        :return: average grade
        """
        if len(self.__grades) > 0:
            return sum(self.__grades) / len(self.__grades)
        return 0.0

    def maximum_grade(self):
        """
        Calculate maximum grade of the student.
        :return: average grade
        """
        if len(self.__grades) > 0:
            return max(self.__grades)
        return 0.0

    def minimum_grade(self):
        """
        Calculate minimum grade of the student.
        :return: average grade
        """
        if len(self.__grades) > 0:
            return min(self.__grades)
        return 11.0
