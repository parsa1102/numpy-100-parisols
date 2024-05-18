import numpy as np

arr = 5 * np.random.default_rng().random(10) + 5
print(arr)

print(np.floor(arr, arr), arr)
print(arr.astype(np.int64))
print(np.trunc(arr))
print(arr // 1)
print(arr - (arr % 1))