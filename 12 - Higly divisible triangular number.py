# Other interesting problem who use dynamic programming/ memoization

import math

n = 500
i = 2
nbDivisor = 0
ans = 0
triangular = 1

while nbDivisor <= 500 and i < 1000000:
    triangular += i
    nbDivisor = 2
    if triangular % 2:
        for j in range(3, int(math.sqrt(triangular))+1, 2):
            if triangular % j == 0:
                nbDivisor += 2
    else:
        for j in range(2, int(math.sqrt(triangular))+1):
            if triangular % j == 0:
                nbDivisor += 2
    '''if nbDivisor > ans:
        ans = nbDivisor'''
    i += 1
    
print(triangular, nbDivisor)