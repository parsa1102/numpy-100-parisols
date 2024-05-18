def generator(size) : 
    ret = []
    import random
    for i in range(size) :
        ret.append(random.randint(1, 20))
    return ret

import numpy as np

arr = np.fromiter(generator(10), dtype=np.int64)

print(arr)