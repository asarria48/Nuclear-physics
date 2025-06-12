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


alpha_fixed = 0.5                 # [fm^-1] 
V0_vals = [20, 50, 80, 100, 200]  # [MeV·fm]


plt.figure(figsize=(10, 6))
for V0 in V0_vals:
    ds_do = angulardist(q, V0, alpha_fixed)
    plt.plot(np.degrees(theta), ds_do, label=f"$V_0$ = {V0} [MeV·fm]")


plt.xlabel("Scattering angle θ [degrees]")
plt.ylabel(r"$\frac{d\sigma}{d\Omega}$ [fm$^2$/sr]")
plt.title(f"Elastic angular distribution (Born), $\\alpha$ = {alpha_fixed} fm$^{{-1}}$")
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('dsdoalphafixed.png')
plt.show()
