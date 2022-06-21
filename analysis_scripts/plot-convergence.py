import numpy as np
import matplotlib.pyplot as plt

F = np.loadtxt('convergence.dat')

plt.plot(F[:,0], F[:,1],'b-', label='A6-DNA')
plt.xlabel("Simulation time (ns)",fontsize=16)
plt.ylabel("RMSD of PMF (kcal/mol)",fontsize=16)
plt.legend(fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(0,5)
plt.tight_layout()
plt.show()
#plt.savefig('convergence-DNA-RNA.png',dpi=800)
