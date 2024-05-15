import numpy as np

A = np.arange(5 , 15)
B = np.arange(1, 10)

print("finding intersections of : \n", A, "\n and \n", B)

print(np.intersect1d(A, B))