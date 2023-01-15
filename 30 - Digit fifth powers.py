n = 5
ans = []
i = 2

'''for i in range(2,500_000):
    if sum(int(j) ** n for j in str(i)) == i:
        ans.append(i)'''

while sum(int(9) ** n for j in str(i)) >= i:
    if sum(int(j) ** n for j in str(i)) == i:
        ans.append(i)
    i += 1

print(sum(ans),ans)