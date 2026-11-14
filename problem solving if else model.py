n=int(input("enter the cost:"))
if n >500:
    print("GST:",n*7/100)
    print("total cost",n+n*7/100)
else:
    print("GST:0")
    print("total amount",n)

