import math

primes = [2,3,5,7,11,13]
primesSum = 41
i = 15
while i < 2000000:
    b = 0
    for j in range(3, int(math.sqrt(i)) + 1, 2):
        if i % j == 0:
            b = 1
            break
    if b == 0:
        primesSum += i
    i += 2

print(primesSum)