prices=[1000,50,-700,0,450]
discount=10
def apply_discounts(prices,discount):
    M=[]
    for i in prices:
        if i>10:
            i*discount/100
            M.append(i)
    return i
a=apply_discounts(prices,discount)
print(a)
