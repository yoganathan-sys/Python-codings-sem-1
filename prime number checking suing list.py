L=[6,9,10,11,16,5,13,8,7]
for i in L:
    for j in range(2,i):
        if(i%j==0):
            break
        else:
            print(i)
