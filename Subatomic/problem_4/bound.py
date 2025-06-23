import numpy as np
import matplotlib.pyplot as plt

hbar_c = 197.327  # [MeV*fm]
m_p = 938.3       # [MeV/c^2] proton's mass 
m_n = 939.6       # [MeV/c^2] neutron's mass
mu = (m_p*m_n)/(m_p+m_n)  # [MeV/c^2] reduced mass 

# parameters of the square well potential
V0 = 35.0         # [MeV] depth of the well
a = 2.0           # [fm] radius of the well
E = -2.224        # [MeV] energy (bound state, for the deuteron)


k = np.sqrt(2*mu*(V0+E))/hbar_c  # inside the well (E is already negative)
kappa = np.sqrt(2*mu*(-E))/hbar_c  # outside the well

# normalization 
A = 1
B = A*np.sin(k*a)/np.exp(-kappa*a)

# radial domain to plot
r_inside = np.linspace(0, a, 300)
r_outside = np.linspace(a, 10, 300)

u_inside = A*np.sin(k*r_inside)           # wavefunction inside the well
u_outside = B*np.exp(-kappa*r_outside)    # wavefunction outside the well


plt.plot(r_inside, u_inside, color='palevioletred', label=r"$u_0(r)$ inside the well")
plt.plot(r_outside, u_outside,color='darkorange',label=r"$u_0(r)$ outside the well")
plt.axvline(x=a, color='gray', linestyle='--', label=r"$r = a$")
plt.xlabel(r"$r$ [fm]")
plt.ylabel(r"$u_0(r)$")
plt.legend()
plt.grid(True)
plt.savefig('bound.png')
plt.show()
