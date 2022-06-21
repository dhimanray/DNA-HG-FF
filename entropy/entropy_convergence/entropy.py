import numpy as np

l = np.loadtxt('eigenval.dat')

l = l.T

lam = l[1]

#temperature
T = 298.0
kB = 0.6/300.0 #kcal/mol
#calculate entropy
S = 0.0

#f1=open('entropy_modes.dat','w')
for i in range(len(lam)):
    if lam[i] >= 1E-12 :
        wi = np.sqrt(1.0/lam[i])    #convert nm^2 to A^2
        #---------------------------------------
        #In SI unit wi = (np.sqrt(1.0/lam[i]))*1.569*1E+13
        #hbar/kBT = 0.2566*1E-13
        #hbar*wi/kBT = 0.4025 * wi
        #----------------------------------------------
        #a = 1.64*1E-14 * wi
        a = 0.4025 * wi

        #Classical entropy
        # S_i = 1.0 + 0.5*np.log(1./(a**2))

        #Andricioaei-Karplus formula (JCP 2001)
        S_i = a/(np.exp(a)-1.0) - np.log(1-np.exp(-a))

        #Schlitter formula
        #S_i = 0.5*np.log(1.0 + (np.exp(1.0)/a)**2)

        S += S_i*kB
        #print(i,S,file=f1)
    else :
        pass

print(S)
