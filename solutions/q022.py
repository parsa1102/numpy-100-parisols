import numpy as np

arr = np.random.random(5 * 5) .reshape(5, 5)
print("original : " , arr)
arr = (arr - arr.mean()) / arr.std()
print("normalized : ", arr)