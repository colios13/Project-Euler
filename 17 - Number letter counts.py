wordNumber = {90:6, 80:6, 70:7, 60:5, 50:5, 40:5, 30:6, 20:6, 19:8, 18:8, 17:9, 16:7, 15:7, 14:8, 13:8, 12:6, 11:6, 10:3, 9:4, 8:5, 7:5, 6:3, 5:4, 4:4, 3:5, 2:3, 1:3}
n = 1000
ans = 0 

for i in range(1,n+1):
    c = i
    andB = 0 #mean and word and B = boolean if true and is already present
    if c >= 1000:
        ans += 8 + wordNumber.get(c//1000)
        c %= 1000
    if c >= 100:
        ans += 7 + wordNumber.get(c//100)
        c %= 100
    for j in wordNumber:
        if c == 0:
            break
        if c >= j:
            if i > 100 and andB == 0:
                ans += 3
                andB = 1
            ans += wordNumber.get(j)
            c -= j
print(ans)