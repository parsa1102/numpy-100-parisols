import numpy as np


A = np.random.random(10)
B = np.random.random(10)

print(np.array_equal(A, B))

#this one would acctually return true if all elements are extremely close to each other but not equal
print(np.allclose(A, B))