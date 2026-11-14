def yoga(n):
    if n==1:
        return n
    else:
        return n*yoga(n-1)
n=int(input("enter the number;"))
print(yoga(n))
