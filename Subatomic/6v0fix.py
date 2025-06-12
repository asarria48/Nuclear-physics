import numpy as np
import matplotlib.pyplot as plt


hbarc = 197.32          # [MeV·fm]
mp = 938.27             # [MeV/c^2] proton's mass
mn = 939.56             # [MeV/c^2] neutron's mass
mu = mp*mn/(mp+mn)      # [MeV/c^2] reduced mass of the n-p system
k = 1.0                 # [fm^-1] transfered wave number


theta = np.linspace(0, np.pi, 1000)     # different scattering angles
q = 2*k*np.sin(theta/2)                 # [fm^-1] momentum transference


def angulardist(q, V0, alpha):
    return ((2*mu*V0)/(hbarc**2))**2*(1/(alpha**2 + q**2)**2)


V0_fixed = 10                               # [MeV·fm]
alpha_vals = [0.3, 0.5, 0.7, 1.2, 1.8]      # [fm^-1] 


plt.figure(figsize=(10, 6))
for alpha in alpha_vals:
    ds_do = angulardist(q, V0_fixed, alpha)
    plt.plot(np.degrees(theta), ds_do, label=f"$\\alpha$ = {alpha} [fm$^{{-1}}$]")


plt.xlabel("Scattering angle θ [degrees]")
plt.ylabel(r"$\frac{d\sigma}{d\Omega}$ [fm$^2$/sr]")
plt.title(f"Elastic angular distribution (Born), V0 = {V0_fixed} MeV·fm")
plt.yscale("log")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('dsdov0fixed.png')
plt.show()
