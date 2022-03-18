import numpy as np
n = 1000
wartosci = []
for i in range(n):
    temp = 0
    for j in range(12):
        temp = temp + np.random.rand()
        wartosci.append(temp - 6)

print(wartosci)
