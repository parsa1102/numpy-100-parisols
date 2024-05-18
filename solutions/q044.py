import numpy as np

def convert(cor) :
    x = cor[0]
    y = cor[1]
    cor[0] = np.sqrt((x*x) + (y*y))
    cor[1] = np.arctan(y*x)
    return cor


arr = np.random.random(10 * 2).reshape(10, 2)
print(arr)


for i in range(10) :
    arr[i] = convert(arr[i])
    
print(arr)