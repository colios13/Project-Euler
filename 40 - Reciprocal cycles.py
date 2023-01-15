# Reciprocal cycles not champernowne
# Cycle detection remind me as always to the tortoise and hare algorithm from Floyd Warshall
# So now try to implement it and adapt it to our need
# This algo work for a linked list not sure it can fit ot our needs
# Idea :
# -  if array[0:len(array)//2] == array[len(array)//2:] cycle = len(array//2)
# That will only find the first cycle if it's start form the first element 


n = 1000
ans = 0

for i in range(2,11):
    num = 1/i
    decimal = [int(v) for i, v in enumerate(str(num)) if i > 1] 
    j = 0
    k = 2
    b = 0 # b always mean boolean
    longestCurLoop = 0    
    print(decimal)
    while k < len(decimal)-1 and b == 0:
        print(decimal[0:k//2], decimal[k//2:k])
        if decimal[0:k//2] == decimal[k//2:k]:
            longestCurLoop = k//2
            break
        j += 1
        k += 2
    if longestCurLoop > ans:
        ans = longestCurLoop

