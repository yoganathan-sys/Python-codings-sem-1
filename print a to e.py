x=ord('A')
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(x),end=" ")
        x+=1
    print()
