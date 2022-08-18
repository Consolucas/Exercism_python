def leap_year(year):
    if (year % 4 == 0) and (year % 100 == 0) and (year % 400 > 0):
        return False
        #return f'{year} is not leap year'
    elif (year % 4 == 0):
        return True
        #return f'{year} is leap year'
    else:
        return False
        #return f'{year} is not leap year'
