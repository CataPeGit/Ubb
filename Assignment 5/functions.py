import re
from collections import Counter

# Sort passagers by full string function:


def sort_passenger_full_string(passenger_name_list):
    # sorting passager by name in alphabetical order
    passenger_name_list.sort()
    return passenger_name_list


# Sort passagers by last name function:
def sortSur(nameList):
    # sort list by last name
    nameList.sort(key=lambda x: x.split()[-1])
    return nameList


# Sort planes according to the number of passengers function:
def bubble_sort(planes_repository):
    # bubble sort algorithm
    n = len(planes_repository)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if len(planes_repository[j].get_passager_list()) > len(planes_repository[j+1].get_passager_list()):

                planes_repository[j], planes_repository[j +
                                                        1] = planes_repository[j + 1], planes_repository[j]
                already_sorted = False

        if already_sorted:
            break

    return planes_repository


# Sort planes according to the number of passengers with the first name starting with a given substring
def bubble_sort_for_substring_given(planes_repository, substring):
    # bubble sort algorithm
    n = len(planes_repository)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if len(planes_repository[j].get_passager_list_with_substrings(substring)) > len(planes_repository[j+1].get_passager_list_with_substrings(substring)):

                planes_repository[j], planes_repository[j +
                                                        1] = planes_repository[j + 1], planes_repository[j]
                already_sorted = False

        if already_sorted:
            break

    return planes_repository


def find_substring(name, substring):
    # checks if a substring is present in a string or not
    if (substring in name):
        y = "^" + substring
        x = re.search(y, name)
        if x:
            return True
        else:
            return False
    else:
        False


# Sort planes according to the string obtained by concatenation
# of the number of passengers in the plane and the destination
def bubble_sort_for_concatenation(planes_repository):
    # bubble sort algorithm

    n = len(planes_repository)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if len(planes_repository[j].get_string_by_concatenation()) > len(planes_repository[j+1].get_string_by_concatenation()):

                planes_repository[j], planes_repository[j +
                                                        1] = planes_repository[j + 1], planes_repository[j]
                already_sorted = False

        if already_sorted:
            break

    return planes_repository


# Identify planes that have passengers with
# passport numbers starting with the same 3 letters
def search_planes_by_passport_letters(planes_repository):
    result = []

    for plane in planes_repository:
        # we will create a list of all passport starting with the 3 letters
        # then we will check if two of the starting 3 letters are the same
        passengers = plane.get_passager_list_as_object()
        list_of_passports = []

        for passenger in passengers:
            passport = passenger.get_passport_number()
            list_of_passports.append(passport[:3])

        identified = [item for item, count in Counter(
            list_of_passports).items() if count > 1]

        if len(identified) > 0:
            result.append(plane)

    if len(result) > 1:
        print(f"Identified planes id's are: ")
        for plane in result:
            print(plane.get_id())
    elif len(result) == 1:
        print(f"Identified plane has id: ")
        for plane in result:
            print(plane.get_id())
    else:
        print("No plane identified.")


# Identify passengers from a given plane for which the first name
# or last name contain a string given as parameter
def search_passengers_containing_string(given_plane, string_searched):
    list_of_passengers = given_plane.get_passager_list()
    result = []
    for name in list_of_passengers:
        name_lower = name.lower()
        string_searched_lower = string_searched.lower()
        if name_lower.find(string_searched_lower) != -1:
            result.append(name)
    if len(result) > 0:
        print(f"Identified passengers are: { result }")
    else:
        print("No passenger identified.")


# Identify plane/planes where there is a passenger with given name
def search_planes_with_passenger(planes_repository, given_name):
    result = []

    for plane in planes_repository:
        names = plane.get_passager_list()
        for name in names:
            name_lower = name.lower()
            given_name_lower = given_name.lower()
            if name_lower.find(given_name_lower) != -1:
                result.append(plane.get_id())
                break

    if len(result) > 1:
        print(f"Identified planes id's are: { result }")
    elif len(result) == 1:
        print(f"Identified plane has id: { result }")
    else:
        print("No plane identified.")


def binary_search(sorted_list, elem):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        middle = (low + high)//2
        if sorted_list[middle] == elem:
            return middle
        elif sorted_list[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1


def bubblesort(lst):
    n = len(lst)
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap = True
        if swap == False:
            break
    print(lst)
