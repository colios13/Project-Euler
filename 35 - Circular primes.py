# The idea for solving this problem was quite easy
# so it's just about optimization for getting a decent time
# I use dict here but should use set for saving some place
# primes as a list vs dict 75s => 7.5s
# Now the most of the time is used for compute primes i know there is a known algorithm for that
# Try to improve my own with some other user implementation and after try to understand the famous algo 
import time
import itertools
from collections import deque


startTime = time.time()
n = 1_000_000
primes = {2:1}
circularPrimes = []

for i in range(3,n,2):
    b = 0
    if i % 2:
        for j in range(3, int(i**0.5) + 1, 2):
            if i % j == 0:
                break
        else:
            primes.update({i:1})

midTime = time.time()

while len(primes) > 0:
    bb = 0
    i = next(iter(primes))
    if i in [11]:
        bb = 1 # print debug enabled
    num = deque([a for a in str(i)])
    permutation = set()
    b = 0
    for _ in range(len(num)):
        num.rotate(-1)
        permutation.add(int(''.join(num)))
    for k in permutation:
        if bb: print(k, k in primes, primes.get(k))
        if k not in primes:
            b = 1
        else:
            del primes[k]
    if b == 0:
        for k in permutation:
            circularPrimes.append(k)


print(len(circularPrimes), circularPrimes[:25], len(primes), str(round(midTime-startTime,2))+'s', str(round(time.time()-startTime,2))+'s')