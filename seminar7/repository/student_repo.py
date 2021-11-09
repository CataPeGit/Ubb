from domain.student_list import Student


class StudentRepository:
    def __init__(self, student_list=[]):
        # check if id of each student is unique
        self.students = student_list.copy()

    def __str__(self):
        """
        Converting a StudentRepository object into a string.
        :return:
        """
        repr_str = f"Number of student in the list: {self.get_number_of_students()}\n"
        for student in self.students:
            repr_str += str(student) + "\n"
        return repr_str

    def __eq__(self, other):
        """
        Check if the parameter is equal to the current object.
        :param other: another StudentRepository object
        :return: boolean: true if the attributes of the two object are equal, false otherwise
        """
        equal = True
        if self.get_number_of_students() != other.get_number_of_students():
            return False
        else:
            for index in range(self.get_number_of_students()):
                equal &= self.students[index] == other.students[index]
            return equal

    def id_exists(self, student_id):
        """
        Verify if a student id is already in the list.
        :param student_id:
        :return: boolean
        """
        for i in range(len(self.students)):
            if self.students[i].get_id() == student_id:
                return True
        return False

    def add_student(self, new_entry: list):
        """
        Seminar 6. (1)
        Add a new student to the repository.
        :param new_entry: list containing the name, group, grades and id of the student

        :raises IndexError if id already exists in the repository
        :raises ValueError if grade is not between 1 and 10
        """
        if self.id_exists(new_entry[3]):
            raise IndexError("ID already exists in the repository")
        self.students.append(Student(new_entry[0], new_entry[1], new_entry[2], new_entry[3]))

    def insert_student(self, index, name, group, grades, student_id):
        """
        Seminar 6. (2)
        Insert a student in the repository on the given index.
        :param index: index where the student will be inserted
        :param name: name of the student
        :param group: group of the student
        :param grades: list of grades of the student
        :param student_id: id of the student (integer)
        """
        if 0 <= index <= len(self.students):
            self.students.insert(index, Student(name, group, grades, student_id))
        else:
            raise IndexError(f"The index should be between 0 and {len(self.students)}, but {index} got.")

    def get_number_of_students(self):
        """
        Seminar 6. (3)
        Get the number of students in the list.
        :return: number of students
        """
        return len(self.students)

    def get_index_student_with_id(self, student_id):
        """
        Seminar 6. (4)
        Get the index of the student with the given ID
        :param student_id:
        :return: index of the student who has the given ID
        """
        for i in range(len(self.students)):
            if self.students[i].get_id() == student_id:
                return i
        return -1

    def get_all_students(self):
        """
        Seminar 6. (5)
        Returns all the students
        :return: list of students
        """
        return self.students

    def get_student_at_index(self, index):
        """
        Seminar 6. (6)
        Get the student at a given index
        :param index: index of the student
        :return: Student instance which is at the given index in the repository
        """
        if 0 <= index < len(self.students):
            return self.students[index]
        else:
            raise IndexError("Index is out of bounds!")

    def get_student_by_id(self, student_id):
        """
        Seminar 6. (7)
        Get the student by his/her ID
        :param student_id: id of the student
        :return: Student instance which has the given ID
        """
        index = self.get_index_student_with_id(student_id)
        if index != -1:
            return self.students[index]
        else:
            raise ValueError(f"ID {student_id} is not in the list")

    def get_students_with_value_less(self, value):
        """
        Seminar 6. (8)
        Get students with grade less than the given value
        :param value: given limit value
        :return: new StudentRepository containing students who have grade smaller than the given value
        """
        result = StudentRepository()
        for student in self.students:
            if student.minimum_grade() < value:
                result.add_student([student.get_name(), student.get_group(), student.get_grades(), student.get_id()])
        return result

    def update_at_index(self, index, name, group, grades):
        """
        Seminar 6. (9)
        Update student at the given index with the given values
        The ID of the student shouldn't change
        :param index: index of the student
        :param name: new name of the student
        :param group: new group of the student
        :param grades: new grade list of the student
        """
        if 0 <= index < len(self.students):
            self.students[index].set_name(name)
            self.students[index].set_group(group)
            self.students[index].set_grades(grades)
        else:
            raise IndexError("Index is out of bounds!")

    def update_by_id(self, student_id, name, group, grades):
        """
        Seminar 6. (10)
        Update student by a given id with the given values
        The ID of the student shouldn't change
        :param student_id: ID of the student
        :param name: new name of the student
        :param group: new group of the student
        :param grades: new grade list of the student
        """
        index = self.get_index_student_with_id(student_id)
        if 0 <= index < len(self.students):
            self.students[index].set_name(name)
            self.students[index].set_group(group)
            self.students[index].set_grades(grades)
        else:
            raise ValueError(f"ID {student_id} is not in the list")

    def delete_at_index(self, index):
        """
        Seminar 6. (11)
        Delete student at the given index
        The ID of the student shouldn't change
        :param index: ID of the student
        """
        if 0 <= index < len(self.students):
            del self.students[index]
        else:
            raise IndexError("Index is out of bounds!")

    def delete_by_id(self, student_id):
        """
        Seminar 6. (12)
        Delete student with the given ID
        The ID of the student shouldn't change
        :param student_id: ID of the student
        """
        index = self.get_index_student_with_id(student_id)
        if 0 <= index < len(self.students):
            del self.students[index]
        else:
            raise ValueError(f"ID {student_id} is not in the list")

    def get_students_with_maximum_average_grade(self):
        """
        Seminar 7. (1)
        :return:
        """
        result = 0
        for student in self.students:
            if len(student.get_grades()) > 0:
                student_grade_average = student.average_grade()
                if student_grade_average >= result:
                    result = student_grade_average
        student_list = StudentRepository()
        for student in self.students:
            if len(student.get_grades()) > 0:
                if sum(student.get_grades()) / len(student.get_grades()) == result:
                    student_list.add_student([student.get_name(), student.get_group(), student.get_grades(), student.get_id()])
        return student_list

    def get_students_with_maximum_grade(self):
        """
        Seminar 7. (2)
        :return:
        """
        result = 0
        for student in self.students:
            if (len(student.get_grades()) > 0):
                student_maximum_grade = student.maximum_grade()
                if (student_maximum_grade >= result):
                    result = student_maximum_grade
        student_list = StudentRepository()
        for student in self.students:
            if student.maximum_grade() == result:
                student_list.add_student([student.get_name(), student.get_group(), student.get_grades(), student.get_id()])
        return student_list

    def get_student_from_group(self, group):
        """
        Get all student from the given group
        :param group: number of the group
        :return: new StudentRep
        ository containing the students of a group
        """
        student_list = StudentRepository()
        for student in self.students:
            if student.get_group() == group:
                student_list.add_student([student.get_name(), student.get_group(), student.get_grades(), student.get_id()])
        return student_list

    def get_average_grade_of_maximums_from_same_group(self, group):
        """
        Seminar 7. (3)
        Calculating the average of maximum grades of students from the same group
        :param group: number of the group
        :return: average grade of maximums
        """
        student_list = self.get_student_from_group(group)
        count = 0
        sum = 0
        for student in student_list.get_all_students():
            if student.maximum_grade() != 0:
                count += 1
                sum += student.maximum_grade()
        if count != 0:
            return sum / count
        else:
            return 0

    def get_minimum_grade_from_group(self, group):
        """
        Seminar 7. (4)
        Calculating the minimum grade of students from the given group
        :param group: number of the group
        :return: minimum grade of students
        """
        studen_list = self.get_student_from_group(group)
        min_grade = 11
        for student in studen_list.get_all_students():
            if student.minimum_grade() < min_grade:
                min_grade = student.minimum_grade()
        if min_grade == 11:
            raise ValueError("No grades available")
        return min_grade
