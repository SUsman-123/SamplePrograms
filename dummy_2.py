'''
import numpy as np
# o -D array
a = np.array(54)
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.itemsize)
print(a.size)
print("=====================================================")

# 1 -D array
a= np.array([1,2,3])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.itemsize)
print(a.size)
print("=====================================================")

# 2 -D array
a= np.array([[1,2,3],[4,5,6]])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.itemsize)
print(a.size)
print("=====================================================")

# 3 -D array
a = np.array([ [[1,2,3],[4,5,6]],[[7,8,9],[0,1,2]] ])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.itemsize)
print(a.size)
print("=====================================================")


a = np.array([1,2,3])
b = np.array([4,5,6])
print(a*b)


import numpy as np
a = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(a[0,1])
print(a[1,2])
print(a[0, 0: 4: 2])
print(a[:, 0: 4: 2])
print(a[:,3])
#print(array_x[0, 0: 4: 2])'''

import numpy as np
array_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
#print(array_3d)
#print(array_3d[0,1,0])
#print(array_3d[:, 1, 1])
print(array_3d[:,:,0])
















