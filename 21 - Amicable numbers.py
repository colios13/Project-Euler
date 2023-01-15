n = 10000
divisorSum = []
amicableNum = []

for i in range(0, n):
    divisor = [j for j in range(1,i//2+1) if i % j == 0]
    if 1 not in divisor:
        divisor = [1] + divisor
    if sum(divisor) < len(divisorSum) and i == divisorSum[sum(divisor)]:
        amicableNum.append(sum(divisor))
        amicableNum.append(i)
    divisorSum.append(sum(divisor))

print(sum(amicableNum), amicableNum)