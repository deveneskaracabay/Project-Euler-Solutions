# Problem 16
# Power digit sum
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?
def problem16(power=1000):
    result = str(2**power)
    total = 0
    for index in result:
        total += int(index)
    return total
print(problem16())
# answer = 1366
