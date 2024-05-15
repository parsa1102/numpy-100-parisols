import numpy as np

arr = np.zeros(9 * 9)
arr[1::2] = 1
print(np.delete(np.delete(arr.reshape(9, 9), -1, 1), -1, 0))