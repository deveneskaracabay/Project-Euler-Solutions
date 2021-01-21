# Problem 20
# Factorial digit sum
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
def problem20(number=100):
    primeList = []
    for n in range(2,number+1):
        i=2
        while n!=1:
            if n%i==0:
                primeList.append(i)
                n /= i
                while True:
                    if n%i==0:
                        primeList.append(i)
                        n /= i
                        continue
                    break
            i+=1
    primeList = sorted(primeList)
    i=0
    while i<len(primeList):
        if primeList[i]==5:
            primeList.pop(i)
            primeList.remove(2)
        else: i+=1
    total = 1
    for i in primeList:
        total*=i
    result = 0
    for i in str(total):
        result += int(i)
    return result
print(problem20())
# answer = 648
