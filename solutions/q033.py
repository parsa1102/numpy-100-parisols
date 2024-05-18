import numpy as np

today = np.datetime64('today')
tommorow = today + np.timedelta64(1)
yesterday = today - np.timedelta64(1)

print('yesterday : ', yesterday)
print('today : ', today)
print('tommorow : ', tommorow)
