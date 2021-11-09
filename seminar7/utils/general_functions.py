def get_maximum_grade(students):
    """
    Find the maximum grade of all student
    :param students: list of students
    :return:
    """
    if len(students) == 0:
        return None
    else:
        max_grade = students[0][1]
        # students[start:end] = students[start], students[start + 1], ..., students[end - 1]
        for student in students[1:]:
            if student[1] > max_grade:
                max_grade = student[1]
        return max_grade
