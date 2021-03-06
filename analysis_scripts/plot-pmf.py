import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

N = 200 #number of points for plotting/interpolation

m = 40   #number of contours

x, y, z = np.genfromtxt(r'pmf-files/pmf87', unpack=True)

xi = np.linspace(x.min(), x.max(), N)
yi = np.linspace(y.min(), y.max(), N)
zi = scipy.interpolate.griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

X, Y = np.meshgrid(xi, yi)

fig = plt.figure()
cp = plt.contourf(X, Y, zi, m, cmap='nipy_spectral')
plt.clim(0.0,22.5)
cbar = plt.colorbar(cp)
cbar.set_label('PMF(kcal/mol)',fontsize=16)
#plt.contour(xi, yi, zi, m)
plt.ylabel("$\Theta (\circ)$",fontsize=16)
plt.xlabel("$\chi (\circ)$",fontsize=16)
plt.title("A6-DNA: PDB: 5UZF")
plt.show()

#plt.savefig("A6-DNA-2D-5UZF.pdf")
