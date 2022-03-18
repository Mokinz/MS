import numpy as np
import matplotlib as mpl
# The code requires a working TeX installation to run
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#random.rand rozklad U(0.1)
#random.normal

nmax = 10**6
pmax = 5 * 10**3
N = np.zeros((nmax, ))

a = 2**16 + 3
m = 2**31
c = 0

N[0] = 10**3

for i in range(1, nmax):
    N[i] = (a * N[i - 1] + c) % m
N /= m

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot(N[:pmax-2], N[1:pmax-1], N[2:pmax], '.')
# Labels are interreted by TeX
ax.set_xlabel(r'$U_{k-2}$')
ax.set_ylabel(r'$U_{k-1}$')
ax.set_zlabel(r'$U_{k}$')
ax.view_init(elev=20, azim=60) # matlab-like rotation
plt.show()
