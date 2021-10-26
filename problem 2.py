year = input("Year: ")
days = int(input("Days: "))

def leap_year(year):
    year = int(year)
    if year % 4 == 0:
        return True
    return False

def determine_date(days):
    final_date = ""
    months = 1
    month_days = 0
    
    while days > 0:
        days -= 1
        month_days += 1
        if  month_days == 31:
            month_days = 0
            months += 1
        elif month_days == 29 and leap_year(year) == True and months == 1:
            month_days = 0
            months += 1
        elif month_days == 28 and leap_year(year) == False and months == 1:
            month_days = 0
            months += 1
        elif month_days == 30 and (months == 3 or months == 5 or months == 8 or months == 10):
            month_days = 0
            months += 1       

    
    if months >= 10:
        months = str(months)
    else:
        months = "0" + str(months)
    
    final_date = final_date + str(month_days) + "." + months + "." + year
    
    return final_date

print(determine_date(days))
