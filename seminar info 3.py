def print_menu():
    print("0 - exit program")
    print("1 - print menu")
    print("2 - read a list")
    print("3 - print the list")
    print("4 - print the sum of the elements")
    print("5 - filter numbers that are not multiples of 2")
    print("6 - delete_sequence")
    print("7 - delete even numbers")
    print("8 - shift longest sequence")

def start():
    print_menu()
    a = []
    command = int(input(">>> "))
    while True:     #while command != 0:
        if command == 1:
            print_menu()
        elif command == 2:
            read_list()
        elif command == 3:
            print(list_to_string(a))
        elif command == 4:
            print(sum_of_powers(a))
        elif command == 5:
            print(filter(a))
        elif command == 6:
            print(delete_even_numbers(a))
        elif command == 7:
            print(filter(a))
        elif command == 8:
            print(reorder_list(a))
        elif command == 0:
            break
        else:
            print("command does not exist. Enter a new one.")


#ex a
def read_list():
    """
    Reads a list of natural numbers with a given number of elements
    """
    n = int(input('n='))
    given_list = []
    for i in range(n):
        x = int(input('x='))
        given_list.append(x)
    return given_list

#ex b

def convert(l):
    str_rep = ""
    for i in l:
        str_rep += str(i) + ", "
    return str_rep


#ex c

def verify(n):
    # verify if n is a power of 2
    k = 1
    while k < n:
        k *= 2
    return k == n

def sum_of_powers(l):
    s = 0
    for i in l:
        if verify(i):
            s += i
    return s

#ex d

def filter(l):
    new_list = []
    for i in l:
        if not verify(i):
            new_list.append(i)
    return new_list

#ex e
def delete_sequence(my_list):
    first = -1
    last = -1
    for i in range(len(my_list)):
        if my_list[i] % 2:
            if first == -1:
                first = i
            last = i
    del my_list[first:last+1]

#ex f
def delete_even_numbers(a):
    for element in reversed(a):
        #print (a[element])
        if element % 2 == 0:
            a.remove(element)
            
    return a

#ex g

def longest_sequence(my_list):
    max_length = 0
    maxim_start_index = -1
    current_length = 0
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            current_length += 1
        else:
            if maximum_length < current_length:
                maximum_length = current_length
                maximum_start_index = i - current_length
            current_length = 0
    return maximum_start_index, maximum_length

def reorder_list(l):
    """
    Shift to the beginning of the list
    """
    start_index, length = longest_sequence(l)
    return l[start_index:start_index+length] + l[:start_index] + l[start_index+length:]
    

a = [1,2,3]
a.append([4])

print(a)
"""
def longest_even_numbers(a): # length
    l = 0
    longest = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            l += 1
        else:
            l = 0
        if l > longest:
            start = 
            longest = l
    return longest

def even 


a = [1,2,4,4,3,4,5,6]
print(longest_even_numbers(a))


l = read_list()
d = convert(l)
print(d)
"""
