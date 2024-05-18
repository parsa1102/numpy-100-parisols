import numpy as np


arr = np.random.random(10)
print(arr)


mx = arr.argmax()

arr[mx] = 0

print(arr)