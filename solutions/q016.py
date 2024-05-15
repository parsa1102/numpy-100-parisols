import numpy as np

arr = np.array(4 * 4 * [1]).reshape(4, 4)
print("before : \n", arr)
arr = np.pad(arr, 1)
print("after  : \n", arr)