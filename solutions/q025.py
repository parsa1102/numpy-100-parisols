import numpy as np

arr = np.array([2, 3, 4, 6, 8, 9, 12, 12, 3, 2, 11 , 6, 5])
print("original array : ", arr)

arr[(3 < arr) & (arr < 8)] *= -1
print("negated : ", arr)
