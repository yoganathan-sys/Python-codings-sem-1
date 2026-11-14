import matplotlib.pyplot as plt
data1=[1,2,3,4,5,6,7,8,9,10]
data2=[11,22,33,44,55,66,77,88,99,100]
plt.hist(data1,bins=5,alpha=0.5,color="lightred",edgecolor="black")
plt.hist(data2,bins=5,alpha=0.5,label="Dataset 2")
plt.legend()
plt.show()
