# Project Euler Problem 6
# Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of 
# the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
# Find the difference between the sum of 
# the squares of the first one hundred natural numbers and the square of the sum.
def problem6(limit=100):
    sumSquare = squareSum = sumNumber = 0
    for i in range(limit+1):
        sumNumber += i
        squareSum += i**2
    sumSquare = sumNumber**2
    between = sumSquare - squareSum
    return between
print(problem6())
# answer = 25164150   
