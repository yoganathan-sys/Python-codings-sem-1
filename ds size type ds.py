import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("array",a)
print("dimentions",a.ndim)
print("shape",a.shape)
print("size",a.size)
print("datatype",a.dtype)
print(a.itemsize,"bytes")
print(a.nbytes,"bytes")
t=a.T
print("tranposed array",t)
print("Flags:\n",a.flags)
