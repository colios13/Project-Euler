sqSum = sum(list(range(1,101))) ** 2
sumSq = sum(i ** 2 for i in range(1,101))
print(sqSum-sumSq)