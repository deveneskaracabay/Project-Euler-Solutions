# Project Euler Problem 5
# Smallest multiple
# 2520 is the smallest number 
# that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def problem5(finish=20):
    primeFactors = []
    for number in range(2,finish):
        for i in primeFactors:
            if number%i==0: number/=i
        limit = number
        for i in range(2,int(limit)):
            if number%i==0:
                primeFactors.append(i)
                if number == 1: break
        if number!=1: primeFactors.append(number)
    result=1
    for i in primeFactors:
        result*=i
    return int(result) 
print(problem5())
# answer = 232792560
