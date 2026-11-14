prices=[111,222,-222,-867,345,0,765,0]
def filter_valid_prices(prices):
    L=[]
    for i in prices:
        if i>0:
            L.append(i)
    return L.append(i)
prices=filter_valid_prices(prices)
print(prices)
discount=10
def apply_discount(prices,discount):
    L=[]
    for i in prices:
        a=i-(i*discount/100)
        L.append(a)
    for j in L:
        if j<10:
            L.remove(j)
    return L
prices=apply_discount(prices,discount)
print(prices)
def classify_store(prices):
    a=sum(prices)/len(prices)
if a>100:
    return "Premium Store"
elif a>=50:
    return "Standard Store"
elif a<50:
    return "Budjet Store"
prices=classify_store(prices)
print(prices)
        
