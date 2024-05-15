import numpy as np

arr = np.random.random(10 * 10 * 10).reshape(10, 10, 10)
print("min : ", arr.min())
print("max : ", arr.max())