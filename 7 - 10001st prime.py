import time
import math
startTime = time.time()

primes = [2,3,5,7,11,13]
i = 15
c = 6

while len(primes) < 10001:
    b = 0
    if i % 2 == 0: b = 1
    if b == 0:
        for j in range(3,int(math.sqrt(i)) + 1):
            if i % j == 0:
                b = 1
                break
    if b == 0: 
        primes.append(i) 
        #c += 1
    i+=2
print(primes[-1], str(round(time.time()-startTime,2))+'s')