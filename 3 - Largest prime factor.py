import math

n = 600851475143

ans = 1
for i in range(int(math.sqrt(n)) + 1, 2, -1):
    b = 0
    c = 0
    if n % i == 0:
        if i % 2 == 0:
            b = 1
        if b == 0:
            for j in range(3, i, 2):
                if i % j == 0:
                    c = 1
                    break
        if c == 0 and b == 0:
            ans = i
            break

print(ans)