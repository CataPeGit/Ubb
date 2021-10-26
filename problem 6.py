"""
First we are going to get the information regarding the current date and the birthday of the person
Then we will get the difference between the years and adjust it by the month and day of the month
"""
print("Please import the information regarding the current date: ")
current_day = int(input("Day = "))
current_month = int(input("Month = "))
current_year = int(input("Year = "))

print() 

print("Please import the following information about a person birthday: ")
day = int(input("Day = "))
month = int(input("Month = "))
year = int(input("Year = "))

age = current_year - year

if month > current_month:
    age -= 1
elif month == current_month:
    if day > current_day:
        age -= 1

print(age)

# automatic current date version below:
"""

from datetime import date

current_date = date.today()

print("Please import the following information about a person birthday: ")
day = int(input("Day = "))
month = int(input("Month = "))
year = int(input("Year = "))

age = current_date.year - year

if month > current_date.month:
    age -= 1
elif month == current_date:
    if day > current_date.day:
        age -= 1

print(age)

"""
