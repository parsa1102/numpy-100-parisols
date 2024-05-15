import numpy as np

arr = np.array([-1.54, -2.44, 1.34, 2.75, -1.5, 4.5])
print("original array : " , arr)

arr = np.copysign(np.ceil(abs(arr)), arr)
print("array rounded away from zero : ", arr)