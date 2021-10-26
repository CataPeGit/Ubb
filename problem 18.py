"""
We will create a list of common digits.
Using a second list we will pick the common digits only once.
We will print the length of this second list as well as the variables in it for the result.
"""
def is_digit_common(n, digit):
    while n:
        if n % 10 == digit:
            return True
        n //= 10
    return False
    

def print_commons(l):
    result_list = []
    for i in range(10):
        if i in l:
            result_list.append(i)
    print(len(result_list))

    result = ""
    for i in range(len(result_list)-1):
        result = result + str(result_list[i]) + ","
    result = result + str(result_list[i+1]) 
    print(result)
    return 

def commom_digits_count(n1, n2):
    list_of_common_numbers = []
    
    while n1 > 0:
        if is_digit_common(n2, n1 % 10):
            list_of_common_numbers.append(n1 % 10)
        n1 //= 10
      
    return  print_commons(list_of_common_numbers) 
    

n1 = int(input("Insert first number: "))
n2 = int(input("Insert second number: "))

commom_digits_count(n1, n2)
