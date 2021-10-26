def ones_in_binary(number):
    ones = 0

    while number >= 1:
        if number % 2 == 1:
            ones += 1
        number = number // 2
    return ones


number = int(input("Natural number: "))

print(ones_in_binary(number))
