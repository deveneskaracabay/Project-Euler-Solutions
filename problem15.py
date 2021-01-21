# Problem 15
# Lattice paths
# Starting in the top left corner of a 2×2 grid, 
# and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
def problem15(n=20,m=20):
    sumNM = [*range(1,n+m+1)]
    nm = [*range(1,n+1)]
    nm.extend([*range(1,m+1)])
    result = 1
    for i,j in zip(sumNM,nm):
        result *= i/j
    return int(round(result,0))
print(problem15())
# answer = 137846528820
