# Project Euler Problem 10
# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
def problem10(limit=2000000):
    primesSum = 2
    for number in range(3,limit,2):
        flag = True
        sqrt = int(number**0.5)+1
        for i in range(3,sqrt,2):
            if not number%i:
                flag = False
                break
        if flag: primesSum += number
    return primesSum
print(problem10())
# answer = 142913828922
