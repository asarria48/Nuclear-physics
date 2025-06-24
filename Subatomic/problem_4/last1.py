import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar_c = 197.327  # MeV*fm
mu = 469.459      # MeV/c^2

# Parameters
V0 = 85  # MeV change this values 
a = 2.0  # fm
E_vals = [5, 10, 15]  # MeV, for different collision energies 

r = np.linspace(0.001, 10, 1000)

# Function to compute continuum wavefunction

def continuum_wavefunction(V0, E):
    kappa = np.sqrt(2 * mu * (V0 + E)) / hbar_c      # inside the well
    k = np.sqrt(2 * mu * E) / hbar_c                 # outside the well

    delta = np.arctan((k / kappa) * np.tan(kappa * a)) - k * a

    A = 1.0
    F = A * np.sin(kappa * a) / np.sin(k * a + delta)

    u = np.zeros_like(r)
    for i, ri in enumerate(r):
        if ri <= a:
            u[i] = A * np.sin(kappa * ri)
        else:
            u[i] = F * np.sin(k * ri + delta)

    u /= np.sqrt(np.trapz(u**2, r))
    return u


colors = ['palevioletred', 'black', 'darkorange']

plt.figure(figsize=(8, 6))
for E, color in zip(E_vals, colors):
    u = continuum_wavefunction(V0, E)
    plt.plot(r, u, label=f"E = {E} MeV", color=color)


plt.xlabel("r [fm]")
plt.ylabel("u0(kr)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('conti85.png')
plt.show()
