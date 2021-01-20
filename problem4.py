# Project Euler Problem 4
# Largest palindrome product
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
def problem4(digitNumber=3):
    maxPolindrome = -1,(0,0)
    startPoint  = int("1"+"0"*(digitNumber-1))
    finishPoint = int("9"*digitNumber)+1
    for i in range(startPoint,finishPoint):
        for j in range(i,finishPoint):
            if i*j<=maxPolindrome[0]: continue
            number = str(i*j)
            flag=True
            for x1,x2 in zip(number,reversed(number)):
                if x1!=x2:
                    flag = False
                    break
            if flag:maxPolindrome=i*j,(i,j)
    return maxPolindrome
print(problem4()) # input digit numbers
# answer = 906609 , from 913*993
