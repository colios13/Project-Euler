import math
nbDigit = 10_000_000_000
n = 1000
ans = 0

for i in range(1,n+1):
    ans += pow(i, i, nbDigit)

print(str(ans)[-10:])