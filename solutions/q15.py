import numpy as np

arr = np.array(5*5*[1]).reshape(5, 5)
arr[1:-1, 1:-1] = 0
print(arr)