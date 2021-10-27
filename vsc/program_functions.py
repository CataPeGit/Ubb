# 1 Add the result

def add_number(score_list, value):  # press 1
    """
    adds value into the score_list as last element
    """
    save_list(score_list)
    score_list.append(value)
    return score_list


def insert_number(score_list, index, value):  # press 2
    """
    inserts value inside the list  at the given index
    """
    save_list(score_list)
    if test_insert_number(index, value, score_list) == False:
        print("Wrong input, Please try again!")
        print()
        return

    score_list.insert(index, value)
    return score_list


def test_insert_number(index, value, score_list):
    if index < 0:
        return False
    if index > len(score_list):
        return False
    return True


# 2 Modify the scores in the array
def remove_index(score_list, index):  # press 3
    """
    removes element from the list at the given index
    """
    save_list(score_list)
    del score_list[index]
    return score_list


def remove_between(score_list, from_index, to_index):  # press 4
    """
    removes elements from the start index("from_index") to the final index("to_index")
    """
    save_list(score_list)
    while from_index <= to_index:
        del score_list[from_index]
        to_index -= 1
    return score_list


def replace(score_list, index, new_value):  # press 5
    """
    Replaces the score on position index from score_list with new_value
    """
    save_list(score_list)
    score_list[index] = new_value
    return score_list


# 3 Get the participants with scores having some properties
def less(score_list, value):  # press 6
    """
    get participants with scores less than the given value
    """
    participants = []
    for e in score_list:
        if e < value:
            participants.append(e)
    print()
    return participants


def sorted_by_score(score_list):  # press 7
    """
    Return sorted list of all participants by their score
    """
    score_list = sorted(score_list, reverse=True)

    return score_list


def sorted_higher(score_list, value):  # press 8
    """
    Returns a sorted list of participants with scores higher than "value"
    """
    highers = []
    for elem in score_list:
        if elem > value:
            highers.append(elem)
    return highers


# 4 Obtain different characteristics of participants
def avg(score_list, from_index, to_index):  # press 9
    """
    Returns the average score for participants between the two given index
    """
    how_many = 0
    total_points = 0

    while from_index <= to_index:
        how_many += 1
        total_points += score_list[from_index]
        from_index += 1

    average = total_points / how_many
    return average


def minimum_between(score_list, from_index, to_index):  # press 10
    """
    Get the minimum score of participants between two index
    """
    mini = 999999999999
    while from_index <= to_index:
        if score_list[from_index] < mini:
            mini = score_list[from_index]
        from_index += 1
    return mini


def mul(score_list, value, from_index, to_index):  # press 11
    """
    Returns a list of scores of participants between the two given index,
    whose score are multiples of value
    """
    participants = []

    for score in score_list:
        if score > value and score % value == 0:
            participants.append(score)

    return participants


# 5. Filter values
def filter_mul(score_list, value):  # press 12
    """
    Removes from "score_list" the participants whose score are not multiples of "value"
    """
    participants = []
    for score in score_list:
        if score % value == 0 and score > value:
            participants.append(score)
    score_list = participants.copy()

    return score_list


def filter_greater(score_list, value):  # press 13
    """
    Keeps only participants with scores  higher than "value" in "score_list"
    Removes the others
    """
    save_list(score_list)
    participants = []
    for score in score_list:
        if score > value:
            participants.append(score)
    score_list = participants.copy()
    return score_list


# 6.Undo
def undo():  # press 14
    global score_list, last_score_list
    score_list = last_score_list.copy()
    return score_list


def save_list(score_list):
    global last_score_list
    last_score_list = score_list.copy()
