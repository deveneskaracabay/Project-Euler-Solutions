# Problem 21
# Amicable numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, 
# then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
def problem21(limit=10000):
    number = 0
    divisorsTotalList = []
    while number<limit:
        divisorsTotal = 1
        sqrt = int(number**.5)+1
        for n in range(2,sqrt):
            if number%n==0:
                m=number/n
                if m==n:
                    divisorsTotal += n
                else:
                    divisorsTotal += n + m
        number+=1
        divisorsTotalList.append(int(divisorsTotal))
    amicableNumbers = []
    for i,n in enumerate(divisorsTotalList):
        if i==n: continue
        try:
            if i == divisorsTotalList[n]: 
                amicableNumbers.append(i)
        except:pass
    return sum(amicableNumbers)

print("result : ",problem21())
# answer = 31626
