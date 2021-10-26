"""
We will use a loop to read the numbers and check the property every time, until number 0 is read
If the property is satisfied we will increase the result counter
"""

print("Please read the numbers: ")
n1 = int(input())
result = 0
still_reading = True

def number_of_digits_5(n):
    counter = 0
    while n:
        if n % 10 == 5:
            counter += 1
        n //= 10
    return counter


if n1 == 0:
    still_reading = False
    
while still_reading:
    n2 = int(input())
    if n2 == 0:
        break
    if number_of_digits_5(n1) > number_of_digits_5(n2):
        result += 1

print(result)
