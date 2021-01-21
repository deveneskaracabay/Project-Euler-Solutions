# Problem 19
# Counting Sundays
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
def problem19(startYear=1901,finishYear=2000,dayName="sunday"):
    dayName = dayName.upper()
    days = {
        0:"MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"
    }
    months = { 
        0:"JANUARY", 1:"FEBRUARY", 2:"MARCH", 3:"APRIL", 4:"MAY", 5:"JUNE", 
        6:"JULY", 7:"AUGUST", 8:"SEPTEMBER", 9:"OCTOBER", 10:"NOVEMBER", 11:"DECEMBER" 
    }
    daysOfMonth = { 
        "JANUARY":31, "FEBRUARY":28, "MARCH":31, "APRIL":30, "MAY":31, "JUNE":30, 
        "JULY":31, "AUGUST":31,"SEPTEMBER":30,"OCTOBER":31, "NOVEMBER":30, "DECEMBER":31 
    }   
    
    dayCounter = counter = 0
    for year in range(1900,startYear):
        if year%4==0: daysOfMonth["February"] = 29
        else: daysOfMonth["February"] = 28
        for month in months:
            counter += daysOfMonth[months[month]]
    for year in range(startYear, finishYear+1):
        if year%4==0: daysOfMonth["February"] = 29
        else: daysOfMonth["February"] = 28
        for month in months:
            if days[counter%7]==dayName: dayCounter += 1
            counter += daysOfMonth[months[month]]
    return dayCounter
print(problem19())
# answer = 171
