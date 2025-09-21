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


V0_vals = [20, 50, 100]         # different values for V0
alpha_vals = [0.5, 0.71, 1.0]   # different values for alpha


plt.figure(figsize=(10, 6))
for V0 in V0_vals:
    for alpha in alpha_vals:
        ds_do = angulardist(q, V0, alpha)
        label = f'$V_0$={V0} [MeV·fm], $\\alpha$={alpha} [fm$^{{-1}}]$'
        plt.plot(np.degrees(theta), ds_do, label=label)

plt.xlabel('Ángulo de dispersión θ (grados)')
plt.ylabel(r'$d\sigma/d\Omega$ (fm$^2$/sr)')
plt.title('Distribución angular elástica (aproximación de Born, potencial de Yukawa)')
plt.yscale('log')
plt.legend(fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.savefig('6plot.png')
plt.show()
