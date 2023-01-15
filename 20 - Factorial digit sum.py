n = 100

factorialSum = 0
factorial = n
for i in range(n-1,0,-1):
    factorial *= i

for i in str(factorial):
    factorialSum += int(i) 
    
print(len(str(factorial)))
