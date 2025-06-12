import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


rho = 2.69  # Density [g/cm^3]


E = [0.75, 0.39]              # Geiger and Marsden given range for Ag and Au (air) [cm]
elements = ['Ag', 'Au']                
color_h = ['palevioletred', 'darkorange']         
color_v = ['palevioletred', 'darkorange']         

# Read data from NIST
data = np.loadtxt('aluminum.txt')
x = data[:, 0]           # Kinetic energy [MeV]
y = data[:, 1] / rho     # CSDA range divided into density [g/cm**2] / [g/cm**3] = [cm]


plt.figure(figsize=(10, 8))
plt.loglog(x, y, label=r'$\alpha$ + aire', color='black')
ax = plt.gca()
ax.set_facecolor("#ecf2f5")

legend = []


# Interpolate to find the range
log_interp = interp1d(np.log10(x), np.log10(y), kind='linear', bounds_error=False, fill_value='extrapolate')

for i, (E, mat) in enumerate(zip(E, elements)):
    color = color_h[i % len(color_h)]


    log_y_intersect = log_interp(np.log10(E))
    R = 10**log_y_intersect  # [cm]
    
    R_microns = R * 1e4      # [µm]

    # Dibujar líneas
    plt.axvline(x=E, color=color, linestyle='--', alpha=0.9)
    plt.axhline(y=R, color=color, linestyle='--', alpha=0.7)

    # Añadir entrada a la leyenda
    legend.append(
        f'R = {R_microns:.2f} µm, E = {E:.2f} MeV'
    )


plt.xlim(np.min(x), np.max(x))
plt.ylim(np.min(y), np.max(y))


plt.xlabel('E [MeV]')
plt.ylabel('R/$\\rho$ [cm]')
plt.title('Rango de las partículas $\\alpha$ en Al')


plt.legend([plt.Line2D([], [], color='black'),
            plt.Line2D([], [], color='palevioletred', linestyle='--'),
            plt.Line2D([], [], color='darkorange', linestyle='--')],
           [r'$\alpha$ + Al'] + legend,
           loc='best')

plt.grid(True, which="both", color='lightgray', ls="-", alpha=0.5)
plt.tight_layout()
plt.savefig('aluminum.png', dpi=300)
plt.show()
