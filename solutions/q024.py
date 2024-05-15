import numpy as np

A = np.random.random(5 * 3).reshape(5, 3)
B = np.random.random(3 * 2).reshape(3, 2)

print("multiplying : \n", A, "\n and \n", B)

ret = np.matmul(A, B)

print("result : \n", ret)