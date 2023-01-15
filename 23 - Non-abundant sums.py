import time

startTime = time.time()
n = 28123 # Greatest number not the sum of two abundant number
x = 24 # lowest sum of abundant number
y = 12 # smallest abundant number
abundant = []

# Find all abundant number below (this function take tooooooo much time)
# 30s => 25s => 15s
for i in range(y, n-y, 1): # step of 2 big improve of perf but seems not work in certain case idk why
    #len 6899 vs 6961
    sumDivisor = 0
    if i % 2 == 0:
        sumDivisor += 1
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                sumDivisor += j
            if sumDivisor > i:
                abundant.append(i)
                break
    else:
        for j in range(1, i // 2 + 1, 2):
            if i % j == 0:
                sumDivisor += j
            if sumDivisor > i:
                abundant.append(i)
                break

print(str(round(time.time()-startTime,2))+'s', 'Work !' if sum(abundant) == 97749062 else '!!! Error !!!', sum(abundant))
print(len(abundant))
# And the other naïve approach fro the second function seems too take infinite to compute
# like doing every computation of sum below i(itertools)