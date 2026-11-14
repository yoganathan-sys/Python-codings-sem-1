n=(input("Enter the emp id:"))
s=int(input("enter the basic salary:"))
hra=s*10/100
da=s*50/100
gp=s+hra+da
#deducation
tax=s*5/100
pf=s*10/100
ded=tax+pf
print("basic  salary:",s)
print("house rent allowance:",hra)
print("gp=",gp)
print("tax=",tax)
print("pf=",pf)
print("deducation:",ded)
print("final salary:",gp-ded)
