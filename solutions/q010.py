import numpy as np

arr = np.array([1, 2, 0, 0, 4, 0], dtype=np.int64)
print("indices : " , arr.nonzero()[0])
