n = 100
ans = []

for i in range(2, n+1):
    for j in range(2, n+1):
        if i ** j not in ans:
            ans.append(i ** j)

print(len(ans))
