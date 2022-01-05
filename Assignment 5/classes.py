from classes import Planes, Passenger
from functions import *


def commands():
    print("0  -> quit")
    print("1  -> Show planes information")
    print("2  -> Show passagers information for a given plane")
    print("3  -> Sort the passengers in a plane by last name")
    print("4  -> Sort planes according to the number of passengers")
    print("5  -> Sort planes according to the number of passengers with the first name starting with a given substring")
    print("6  -> Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination")
    print("7  -> Identify planes that have passengers with passport numbers starting with the same 3 letters")
    print("8  -> Identify passengers from a given plane for which the first name or last name contain a string given as parameter")
    print("9  -> Identify plane/planes where there is a passenger with given name")
    print("10 -> Add plane to repository")


def main():

    passager1 = Passenger("Michael", "Jordan", "j23")
    passager2 = Passenger("Kobe", "Bryant", "k24")
    passager3 = Passenger("Rose", "Derrick", "jjj")
    passager4 = Passenger("Lebron", "James", "jjj")
    passager5 = Passenger("Kawhi", "Leonard", "kl2")
    passager6 = Passenger("Jason", "Kidd", "u21")
    passager7 = Passenger("Tony", "Parker", "t25")
    passager8 = Passenger("Tim", "Duncan", "tdm")
    passager9 = Passenger("Larry", "Bird", "lar")
    passager10 = Passenger("Magic", "Johnson", "mag")

    planes_repository = [
        Planes("1", "Tarom", 15, "Cluj-Napoca", [passager1, passager2]),
        Planes("2", "Tarom", 15, "New York", [passager1]),
        Planes("3", "Tarom", 30, "London", [passager2, passager3, passager4]),
        Planes("4", "Tarom", 30, "Paris", [passager2, passager3, passager5]),
        Planes("5", "Tarom", 25, "Paris", [passager6, passager3, passager5]),
        Planes("6", "Tarom", 25, "Paris", [passager2, passager6]),
        Planes("7", "Tarom", 25, "Paris", [passager10]),
        Planes("8", "Tarom", 25, "Paris", [passager7, passager8, passager10]),
        Planes("9", "Tarom", 30, "Paris", [passager1, passager9]),
        Planes("10", "Tarom", 30, "Paris", [passager7, passager9, passager8])
    ]

    while True:
        commands()

        # user picks the command
        comm = int(input("Your command: "))

        if comm == 0:
            quit()

        if comm == 1:
            # show information about the plane
            for plane in planes_repository:
                print(plane.__str__())

        if comm == 2:
            # show information about passengers in a given plane
            id = int(input("Select plane by id: "))
            for plane in planes_repository:
                if plane.get_id() == id:
                    for passenger in plane.get_passager_list_as_object():
                        print()
                        print(f"First name: { passenger.get_first_name()}")
                        print(f"Last name: { passenger.get_last_name()}")
                        print(f"Passport: { passenger.get_passport_number()}")

        if comm == 3:
            # Sort the passengers in a plane by last name
            id = int(input("Select plane by id: "))
            for plane in planes_repository:
                if plane.get_id() == id:
                    plane.sort_passengers_by_last_name()

        if comm == 4:
            # Sort planes according to the number of passengers
            bubble_sort(planes_repository)

        if comm == 5:
            # Sort planes according to the number of passengers with the first name starting with a given substring
            substring = input("Substring: ")
            bubble_sort_for_substring_given(planes_repository, substring)

        if comm == 6:
            # Sort planes according to the string obtained by concatenation
            # of the number of passengers in the plane and the destination
            # should be like "3Toronto" n stuff
            bubble_sort_for_concatenation(planes_repository)

        if comm == 7:
            # Identify planes that have passengers with
            # passport numbers starting with the same 3 letters
            search_planes_by_passport_letters(planes_repository)

        if comm == 8:
            # Identify passengers from a given plane for which the first name
            # or last name contain a string given as parameter
            id = int(input("Select plane by id: "))
            string_searched = input("String you are looking for: ")

            if len(string_searched) > 0:
                for plane in planes_repository:
                    if plane.get_id() == id:
                        given_plane = plane
                        break
                search_passengers_containing_string(
                    given_plane, string_searched)
            else:
                continue

        if comm == 9:
            # Identify plane/planes where there is a passenger with given name
            given_name = input("Searched name is: ")
            search_planes_with_passenger(planes_repository, given_name)

        if comm == 10:
            # Add plane to repository
            id = input("Id: ")
            company = input("Company: ")
            number_of_seats = int(input("Number of seats: "))
            destination = input("Destination: ")
            planes_repository.append(
                Planes(id, company, number_of_seats, destination, []))

        print()


main()

