import numpy as np
a=np.array([1,2,3,4,5,6])
print(a.shape)

#r=a[np.newaxis,:]
#r.shape
b=np.expand_dims(a,axis=1)
b.shape
#c=np.expand_dims(a,axis=0)
#c.shape
