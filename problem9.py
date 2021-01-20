# Project Euler Problem 9
# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
def problem9(number=1000):
    for a in range(1,int(number/2)):
        for b in range(1,int(number/2)):
            c = (a**2+b**2)**0.5
            if str(c).endswith(".0"):
                if int(a+b+c)==number:
                    return a,b,int(c)
print(problem9())# answer = (200, 375, 425)
