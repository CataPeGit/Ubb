import point_list

def print_menu():
    print('0 - exit program')
    print('1 - print menu')
    print('2 - distance between 2 points')
    print('3 - increase x coordinates')
    print('4 - top k closest')
    print('5 - get highest distance')
    print('6 - write to file')
    print('7 - read from file')


def start():
    print_menu()
    command = input('>>> ')
    my_point_list = [[1, 2, 'red'], [3, 3, 'green'], [0, 5, 'red']]
    while command != '0':
        if command == '1':
            print_menu()
        elif command == '2':
            try:
                first_index = int(input('First index: '))
                second_index = int(input('Second index: '))
                print('Distance is: ', point_list.distance(my_point_list, first_index, second_index))
            except IndexError as ie:
                print(ie)
            except ValueError:
                print('Indices must be integer values!')
        elif command == '3':
            try:
                value = int(input('Value: '))
                print(point_list.increase_x(my_point_list, value))
            except ValueError:
                print('Value must be an integer number')
        elif command == '4':
            try:
                index = int(input('Index: '))
                k = int(input('k: '))
                print(f'K closest points to {my_point_list[index]}: {point_list.k_closest(my_point_list, index, k)}')
            except IndexError:
                print('Index out of range')
            except ValueError:
                print('Integers expected')
        elif command == '5':
            print(point_list.highest_distance(my_point_list))
        elif command == '6':
            try:
                filename = input("Filename: ")
                point_list.write_file(my_point_list, filename)
            except IOError:
                print("file error")
        elif command == '7':
            try:
                filename = input("Filename: ")
                my_point_list = point_list.read_file(filename)
                print(my_point_list)
            except IOError:
                print("file error")
            except ValueError:
                print("bad values")
        else:
            print(f'{command} command is not existing!')
        command = input('>>> ')
