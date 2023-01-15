# Start of project Euler 
# First exercice
# 1) Multiples of 3 and 5

a = []
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        a.append(i)
print(sum(a)) 