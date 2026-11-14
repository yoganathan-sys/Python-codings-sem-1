l=[10,3,0,'15','vijay',9]
nl1=list(map(lambda x:type(x)==int,l))
nl2=list(filter(lambda x:type(x)==int,l))
print(nl1,nl2,sep='\n')
