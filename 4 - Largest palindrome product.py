import sys

palindrome = []

for i in range(999,0,-1):
    for j in range(999,0,-1):
        a = str(i * j)
        if a == a[::-1]:
            palindrome.append(a)
            #print(a, i, j)

print(sorted(palindrome, key= lambda x: int(x))[-1])