import numpy as np

arr = np.random.random(10)

arr.flags.writeable = False

#will fail to
arr *= 2

print(arr)