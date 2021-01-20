# Project Euler Problem 3
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def problem3(number=600851475143):
    maxPrime = 0
    limit = number+1
    for i in range(2,limit):
        if number%i==0:
            maxPrime = i
            while True:
                if number%i==0:
                    number /= i
                    continue
                break
            if number == 1: break
    return maxPrime
print(problem3())
# answer = 6857
