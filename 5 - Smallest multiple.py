a = 0
i = 2520
while a == 0 and i < 2000000000:
    for j in range(11,20):
        if i % j != 0:
            break
    else:
        print(i)
        a = 1
    i += 20

'''for i in range(11,20):
    print(i)'''
#20,19,18,17,16,15,14,13,12,11