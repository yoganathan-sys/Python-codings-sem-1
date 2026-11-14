n=int(input("enter the usage:"))
c=int(input("enter amount:"))
a=input("enter the area:")
if n>10 and a=="rural":
    print("offer:",c*50/100)
    print("area",a)
    print("amnt:",c-c*50/100)
elif n<=10 and a=="rural":
    print("offer:",c*25/100)
    print("area:",a)
    print("amnt:",c-c*25/100)
else:
    print("offer:",c*10/100)
    print("area:urban")
    print("amnt:",c-c*10/100)
