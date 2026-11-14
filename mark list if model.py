#MARK SHEET
ta=int(input("Enter your tamil mark:"))
en=int(input("enter your eng mark:"))
m=int(input("enter your math mark:"))
sc=int(input("enter your science mark:"))
s=int(input("enter your social mark:"))
print("tamil mark",ta)
print("english mark",en)
print("maths mark",m)
print("science mark",sc)
print("social mark",s)
total=ta+en+m+sc+s
print("total=",total)
print("avarage=",total/5)
if(ta >=35 and en>=35 and m>=35 and sc>=35 and s>=35):
    print("result=","pass")
else:
    print("fail")
