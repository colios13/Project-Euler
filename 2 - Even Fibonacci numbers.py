a=[1,2]
b=[]

while a[-1] <= 4000000:
    a.append(a[-1]+a[-2])

for i in a:
    if i % 2 == 0:
        b.append(i)
print(sum(b))