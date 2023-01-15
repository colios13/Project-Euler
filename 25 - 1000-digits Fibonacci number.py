n = 1000
fibonacci = [1,1]
i = 2

while len(str(fibonacci[-1])) < n:
    fibonacci.append(fibonacci[0]+fibonacci[1])
    fibonacci.pop(0)
    i += 1

print(i,fibonacci[-1])