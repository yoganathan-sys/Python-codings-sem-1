s=int(input("enter your first choice:"))
if s==8:
    s=int(input("enter the second choice:"))
    print("YOU WON THE GAME")
elif s==7:
    a=int(input("enter the third choice"))
    print("YOU ARE SECOND")
elif s==6:
    print("YOU ARE THIRD")
elif s==5:
    print("YOU ARE FOURTH")
elif s==4:
    print("YOU ARE FIFTH")
elif s==3:
    print("YOU ARE SIXTH")
elif s==2:
    print("YOU ARE SEVENTH")
elif s==1:
    print("YOU ARE EIGHTH")
else:
    print("YOU ARE FAILED BETTER LUCK NEXT TIME",s)
