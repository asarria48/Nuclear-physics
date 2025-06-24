import numpy as np
import matplotlib.pyplot as plt

m1 = 12*931.5           # [MeV/c^2] mass of 12C
m2 = 16*931.5           # [MeV/c^2] mass of 16O
mu = (m1*m2)/(m1+m2)    # masa reducida en MeV/c^2
hbarc = 197.3           # [MeV·fm]

# different values for V0 [MeV] (depth) and alpha [fm^-1]
param_sets = [(70, 0.5),(100, 0.7),(150, 0.9)]

r = np.linspace(0.1, 3, 500)

fig, axes = plt.subplots(3, 3, figsize=(15, 12))
l_values = [0, 2, 4]

for i, (V0, alpha) in enumerate(param_sets):

    def V_yukawa(r):
        return -V0*np.exp(-alpha*r)/r                 # Yukawa's potential

    def V_cent(r, l):
        return (hbarc**2*l*(l+1))/(2*mu*r**2)         # centrifugal potential

    def V_eff(r, l):
        return V_yukawa(r)+V_cent(r, l)             # effective potential


    for j, l in enumerate(l_values):
        ax = axes[i, j]
        ax.plot(r, V_yukawa(r), '-', color='darkorange', label='Yukawa')
        ax.plot(r, V_cent(r, l), '--', color='palevioletred', label=fr'Centrifugal (l={l})')
        ax.plot(r, V_eff(r, l), '-.', color='black', label=fr'$V_{{eff}}$')
        ax.set_ylim(-800, 800)
        ax.set_xlim(0.1, 3)
        ax.set_xlabel('r [fm]')
        ax.set_ylabel(r'$V(r)$ [MeV]')
        ax.grid(True)
        ax.text(2.3, -700, f"$V_0$={V0}, $\\alpha$={alpha}, $l$={l}",
                fontsize=10, ha='right', bbox=dict(facecolor='white', alpha=0.6))
        if i == 0 and j == 2:
            ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig("yukawagrid.png")
plt.show()
