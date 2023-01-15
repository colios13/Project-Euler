import itertools
coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
#coins = [0.01, 0.02, 0.05]
n = 2
ans = []
bruteForce = list(itertools.permutations(coins, len(coins)))

for i in bruteForce:
    num = 0
    for j, a in enumerate(i):
        num += a
        if num >= 2:
            if num == 2 and i[:j+1] not in ans:
                ans.append(i[:j+1])
            break

print(len(ans), ans)

# Think about 2 = 0.01 * 200 so 200 way
# with 0.02 100, 0.05 40, 0.1 20, 0.2 10, 0.5 4, 1 2, 2 1