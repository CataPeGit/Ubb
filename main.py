# Program
from program_functions import *
from UI import *
from tests import *


def command_valid(comm):
    if comm >= 0 and comm <= 15:
        return True
    return False


def main_program():
    commands()
    comm = int(input("Your command : "))
    global score_list, last_score_list
    print()
    #score_list = [0, 1, 2 , 3 , 4 , 5, 6, 7 ,8, 9]

    if command_valid(comm) == False:
        print("Command does not exist! Please enter a valid one.")

    if comm == 0:
        quit()

    elif comm == 1:
        value = int(input("Value to add: "))
        score_list = add_number(score_list, value)

    elif comm == 2:
        index = int(input("Index: "))
        value = int(input("Value to add: "))
        score_list = insert_number(score_list, index, value)

    elif comm == 3:
        index = int(input("Index: "))
        score_list = remove_index(score_list, index)

    elif comm == 4:
        from_index = int(input("Start index: "))
        to_index = int(input("Stop index: "))
        score_list = remove_between(score_list, from_index, to_index)

    elif comm == 5:
        index = int(input("Index: "))
        new_value = int(input("New value: "))
        score_list = replace(score_list, index, new_value)

    elif comm == 6:
        value = int(input("Comparison value: "))
        print("Participants with score less than value are :",
              less(score_list, value))
        print()

    elif comm == 7:
        print()
        print("Participants sorted :", sorted_by_score(score_list))
        print()

    elif comm == 8:
        value = int(input("Comparison value: "))
        print()
        print("Participants with score higher than value are :",
              sorted_higher(score_list, value))
        print()

    elif comm == 9:
        from_index = int(input("Start index: "))
        to_index = int(input("Stop index: "))
        print()
        print("Average is: ")
        print(avg(score_list, from_index, to_index))
        print()

    elif comm == 10:
        from_index = int(input("Start index: "))
        to_index = int(input("Stop index: "))
        print()
        print("Minimum is: ", minimum_between(
            score_list, from_index, to_index))
        print()

    elif comm == 11:
        value = int(input("Comparison value: "))
        from_index = int(input("Start index: "))
        to_index = int(input("Stop index: "))
        print()
        print("Scores are: ", mul(score_list, value, from_index, to_index))
        print()

    elif comm == 12:
        value = int(input("Comparison value: "))
        score_list = filter_mul(score_list, value)

    elif comm == 13:
        value = int(input("Comparison value: "))
        score_list = filter_greater(score_list, value)

    elif comm == 14:
        score_list = undo()

    elif comm == 15:
        run_tests()

    print("Current list: ")
    print(score_list)
    main_program()


global score_list, last_score_list
# we will have the following list as default
score_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
last_score_list = score_list.copy()
main_program()
