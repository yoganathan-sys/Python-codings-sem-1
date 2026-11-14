n=int(input("enter the number:"))
l=int(input("enter the number:"))
m=int(input("enter the number:"))
if n>=m and n>=l:
    print("largest",n)
elif l>=m and l>=m:
    print("largest",l)
else:
    print("largest",m)
print("largest",max(n,l,m))
