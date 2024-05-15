import numpy as np

arr = np.array([1, 2, 3, 4, 5] , dtype=np.int64)


print(np.size(arr))
print(arr.itemsize)

#memmory size = number of items * size of each item on memmory
print(np.size(arr) * arr.itemsize)