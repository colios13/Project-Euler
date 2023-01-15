# Problem where reflexion was needed because naïve solution was too slow so 
# for solve it i have used a dynamic programming approach with dict
# and i think it's the most optimal solution
n = 1000000
maxVal = 0
longestChain = 0
incorrectNum = {}

for i in range(n,1,-1):
    j = i
    c = 0
    currentChain = [i]
    while j != 1:
        if incorrectNum.get(j):
            for k, num in enumerate(currentChain[:-1]):
                incorrectNum.update({num : (len(currentChain[:-1]) - k) + incorrectNum.get(j)})
            c = len(currentChain[:-1]) + incorrectNum.get(j)
            break 
        if j % 2 == 0:
            j //= 2
        else:
            j = j * 3 + 1
        currentChain.append(j)
    else:
        for k, num in enumerate(currentChain):
            incorrectNum.update({num : len(currentChain) - k})
        c = len(currentChain)
    if c > longestChain:
        maxVal = i
        longestChain = c

print(longestChain, maxVal)