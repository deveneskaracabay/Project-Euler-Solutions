# Project Euler Problem 7
# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def problem7(iteration=10001):
    number = 2
    count = 0
    while True:
        flag = True
        sqrtOfNumber = int(number**0.5)+1
        for i in range(2,sqrtOfNumber):
            if not number%i:
                flag = False
                break
        if flag: count+=1
        if count==iteration: return number
        number +=1
        
print(problem7())
# answer = 104743
