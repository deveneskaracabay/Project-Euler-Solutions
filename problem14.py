# Problem 14
# Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
def problem15(limit=1000000):
    maxIteration = 0
    iterList =[0,1]
    for number in range(2,limit):
        count = 1
        copy = number         
        while copy>1:
            if copy<number:
                count += (iterList[int(copy)]-1)
                copy = 0
                break
            if copy%2:
                copy = (3*copy+1)
                count += 1
            else:
                copy /= 2
                count += 1
        iterList.append(count)
    return max(iterList),iterList.index(max(iterList))
print(problem15())
# answer = 525 iteration with 837799
