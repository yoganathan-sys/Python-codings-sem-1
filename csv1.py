import csv
d=open('D:\YOGA.csv','r')
r1=csv.reader(d)
print(*r1,sep='\n')
d.close()
