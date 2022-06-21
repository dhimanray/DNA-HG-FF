import numpy as np
import matplotlib.pyplot as plt

l1 = np.loadtxt('c1-c1-distance.dat')
l2 = np.loadtxt('h-bond-distance.dat')
l3 = np.loadtxt('chi_theta.dat')
print(l1)

fig, ax = plt.subplots()
linw = 2.0
ax.plot(l1[:,0]*0.1, l1[:,1], lw=linw, label="C1'(A)-C1'(T)")
ax.plot(l1[:,0]*0.1, l2[:,1], lw=linw, label="N1(A)-N3(T)")
ax.plot(l1[:,0]*0.1, l2[:,2], lw=linw, label="N7(A)-N3(T)")
ax2 = ax.twinx()
#ax2.set_ylabel('Dihedral angle ($^{\circ}$)',fontsize=16)
#ax2.tick_params(right='off',labelright='off')
ax2.scatter(l1[:,0]*0.1, l3[:,1] - 2.0, lw=0.5, label="$\chi$")
ax2.scatter(l1[:,0]*0.1, l3[:,2] - 2.0, lw=0.5, label="$\Theta$")
ax2.set_ylim(-6,35)
ax2.set_yticks([-5.14,-2,1.14])
ax2.set_yticklabels(['-180$^{\circ}$', '0$^{\circ}$', '180$^{\circ}$'])
ax2.tick_params(labelsize=14)
ax.axvspan(0,4.38,alpha=0.5,color='gray',label='WC')
ax.axvspan(17.6,18.5,alpha=0.5,color='gray')
ax.axvspan(36.0,41.1,alpha=0.5,color='cyan',label='HG')
plt.xlim(0,50)
ax.set_ylim(-5,35)
ax.set_xlabel('Time (ns)',fontsize=20)
ax.set_ylabel('Distance ($\AA$)',fontsize=20)
ax.tick_params(labelsize=14)
#ax.get_xticklabels(fontsize=14)
ax.legend(fontsize=14,ncol=2,shadow=True)
ax2.legend(fontsize=14,ncol=1,loc=2,shadow=True)
plt.tight_layout()
plt.show()
#plt.savefig('traj-DNA.png',dpi=800)
