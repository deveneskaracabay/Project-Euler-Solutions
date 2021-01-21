# Problem 17
# Number letter counts
# If the numbers 1 to 5 are written out in words: 
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?
# NOTE: Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.
def problem17():
    data = {
        0:"",1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
        6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
        11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
        15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
        19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty",
        50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 
        90:"ninety", }
    strNumber = ""
    for number in range(1,1000):
        strNumber += ""
        if number > 99:
            firstD  = number // 100
            secondD = (number%100)//10 
            thirdD  = number%10

            strNumber += data[firstD]+"hundred"
            if number % 100 == 0: continue
            if secondD == 1:
                strNumber += "and"+data[number%100]
                continue
            strNumber += "and"+data[secondD*10]
            if number%10!=0: 
                strNumber += data[thirdD]
        
        elif number > 9:
            if number<20:
                strNumber += data[number]
                continue
            firstD  = number//10
            secondD = number% 10
            strNumber+=data[firstD*10]
            if number%10!=0:
                strNumber+=data[secondD]        
            else:
                strNumber += data[number]
    strNumber += "onethousand"
    return len(strNumber)
print(problem17())
# answer = 21124
