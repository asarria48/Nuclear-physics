import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

rho = 19.32  # Density [g/cm^3]


E = 0.39                    # Energy found in the previous plot [MeV]
element = 'Au'           
color = 'darkorange'          

# NIST data
data = np.loadtxt('gold.txt')
x = data[:, 0]              # Kinetic energy [MeV]
y = data[:, 1] / rho        # CSDA range divided into density [g/cm**2] / [g/cm**3] = [cm]

# I interpolate to find the intersection so we can see the range
log_interp = interp1d(np.log10(x), np.log10(y), kind='linear', bounds_error=False, fill_value='extrapolate')
log_y_val = log_interp(np.log10(E))
R_equiv = 10**log_y_val  

R_microns = R_equiv * 1e4   # turn centimetres into micrometres


plt.figure(figsize=(10, 8))
plt.loglog(x, y, label=r'$\alpha$ + aire', color='black')
ax = plt.gca()
ax.set_facecolor("#ecf2f5")


plt.axvline(x=E, color=color, linestyle='--', alpha=0.7)


plt.axhline(y=R_equiv, color=color, linestyle='--', alpha=0.7)


plt.xlim(np.min(x), np.max(x))
plt.ylim(np.min(y), np.max(y))


plt.xlabel('E [MeV]')
plt.ylabel('R/$\\rho$ [cm]')
plt.title('Rango de las partículas $\\alpha$ en Au')


plt.legend([
    plt.Line2D([], [], color='black'),
    plt.Line2D([], [], color=color, linestyle='--')
], [
    r'$\alpha$ + Au',
    f'E = {E:.2f} MeV, R = {R_microns:.2f} µm' 
], loc='best')

plt.grid(True, which="both",color='lightgray', ls="-", alpha=0.5)
plt.tight_layout()
plt.savefig('gold.png', dpi=300)
plt.show()