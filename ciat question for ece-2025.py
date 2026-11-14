def basic(pay):
    allown=pay*50/100
    return allown
def tax(pay):
    ded=pay*10/100
    return ded
pay=int(input("enter the number:"))
a=basic(pay)
b=tax(pay)
print("total salary:",pay+a-b)
