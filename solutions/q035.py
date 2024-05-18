import numpy as np

A = np.random.randint(1, 1000)
B = np.random.randint(1, 1000)
print(A, B)

print(np.multiply(np.add(A, B), np.divide(-A, 2)))