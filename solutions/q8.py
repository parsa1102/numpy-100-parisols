import numpy as np

arr = np.array([1, 2, 3, 4 , 5], dtype=np.int64)
print("before : " , arr)
arr = arr[::-1]
print("after : ", arr)