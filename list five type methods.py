#1 st method
L=[1,2,3,4,5,"yoga",True]
print(L[2])
#2 nd method
print(L[1:2:3])
#3rd method
L=["yoga",1.2,2,3,4,True]
for i in L:
    print(i)
for i,j in enumerate(L):
    print(i,j)
for i,j in enumerate(L):
    print(i)
#4th method
L=["yoga",1.2,2,3,4,True]
print(*L,sep='\n')
#5th method
L=["yoga",1.2,2,3,4,True]
print(L)

