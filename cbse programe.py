N=[10,12,33,44,85]
for c in range(4,0,-1):
    X=N[c]
    Y=N[c-1]
    if X>Y:
        X=X-Y
    else:
        Y=Y-X
    print(X,Y,sep="",end=' ')
