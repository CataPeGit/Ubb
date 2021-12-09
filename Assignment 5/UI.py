from classes import Planes, Passenger


def commands():
    print("0 -> quit")
    print("1 -> Show planes information")
    print("2 -> Show passagers information")


def main():
    commands()

    passager1 = Passenger("Michael", "Jordan", "23")
    passager2 = Passenger("Kobe", "Bryant", "24")
    planes_repository = Planes(
        1, "Tarom", 15, "Cluj-Napoca", [passager1, passager2])

    while True:

        # user picks the command
        comm = int(input("Your command: "))

        if comm == 0:
            quit()

        if comm == 1:
            print(planes_repository.__str__())

        if comm == 2:
            for passager in planes_repository.get_passager_list():
                print(passager.__str__())

        print()


main()
