print("0-male\n1-female")
N=int(input("enter the gender:")) 
age=int(input("enter the age:"))
weg=float(input("enter the weight:"))
if N==0:
    if age>=18 and weg>=50:
        print("you are a male you are eligible")
    else:
        print("you are a male you are not eligible")
else:
    if age>=18 and weg>=45:
        print("you are female and valid")
    else:
        print("you are female and not valid")
