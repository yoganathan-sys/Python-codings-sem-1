print("jack hotel")
print("1.dhosa\n2.non\n3.butter non\n4.parotta")
choice=int(input("enter your choice:"))
qty=int(input("enter the quantity:"))
if choice==1:
    print("dhosa",qty*100)
elif choice==2:
    print("non",qty*120)
elif choice==3:
    print("butter non",qty*175)
elif choice==4:
    print("parotta",qty*200)
else:
    print("no food")
