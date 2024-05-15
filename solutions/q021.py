import numpy as np

arr1 = np.array([0, 1])
arr1 = np.tile(arr1, 4)
arr2 = np.array([1, 0])
arr2 = np.tile(arr2, 4)
arr = np.append(arr1, arr2)

arr = np.tile(arr, 4)
print(arr.reshape(8, 8))
#print(np.delete(np.delete(arr.reshape(9, 9), -1, 1), -1, 0))