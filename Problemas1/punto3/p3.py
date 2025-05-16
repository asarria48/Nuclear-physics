import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


rho = 0.001204  # Density [g/cm^3]


GM_range = [0.45, 0.30]              # Geiger and Marsden given range for Ag and Au (air) [cm]
elements = ['Ag', 'Au']                
color_h = ['palevioletred', 'darkorange']         
color_v = ['palevioletred', 'darkorange']         

# Read data from NIST
data = np.loadtxt('air.txt')
x = data[:, 0]           # Kinetic energy [MeV]
y = data[:, 1] / rho     # CSDA range divided into density [g/cm**2] / [g/cm**3] = [cm]


plt.figure(figsize=(10, 8))
plt.loglog(x, y, label=r'$\alpha$ + aire', color='black')
ax = plt.gca()
ax.set_facecolor("#ecf2f5")

legend = []


for i, (R, mat) in enumerate(zip(GM_range, elements)):
    color = color_h[i % len(color_h)]

    plt.axhline(y=R, color=color, linestyle='--', alpha=0.9)

    # I interpolate to find the intersection (energy)
    log_interp = interp1d(np.log10(y), np.log10(x), kind='linear', bounds_error=False, fill_value='extrapolate')
    log_x_intersect = log_interp(np.log10(R))
    E = 10**log_x_intersect  


    plt.axvline(x=E, color=color, linestyle='--', alpha=0.7)

    # Añadir entrada a la leyenda
    legend.append(
        f'R = {R:.2f} cm, E = {E:.2f} MeV {mat}'
    )


plt.xlim(np.min(x), np.max(x))
plt.ylim(np.min(y), np.max(y))


plt.xlabel('E [MeV]')
plt.ylabel('R/$\\rho$ [cm]')
plt.title('Rango de las partículas $\\alpha$ en el aire')


plt.legend([plt.Line2D([], [], color='black'),
            plt.Line2D([], [], color='palevioletred', linestyle='--'),
            plt.Line2D([], [], color='darkorange', linestyle='--')],
           [r'$\alpha$ + aire'] + legend,
           loc='best')

plt.grid(True, which="both", color='lightgray', ls="-", alpha=0.5)
plt.tight_layout()
plt.savefig('air.png', dpi=300)
plt.show()
