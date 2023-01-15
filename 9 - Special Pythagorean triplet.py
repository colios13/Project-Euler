import math
import sys

n = 1000
a = b = c = 0
for i in range(n-200, 350, -1):
    j = i-1
    while j + i < n and j < i and 0 < n - (j + i) < j:
        k = n - (j + i)
        if k**2 + j**2 == i**2:
            print(i*j*k)
            sys.exit() 
        j -= 1
    

#print(701**2+702**2, 1000**2)