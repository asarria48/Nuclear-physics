import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

# read the data
theoretical = pd.read_csv('stablenuclei.csv')
experimental = pd.read_csv('EstablesExpNZ.csv')

# rename the data for further use
N_theo = theoretical['N']
Z_theo = theoretical['Z']
N_exp = experimental['N']
Z_exp = experimental['Z']

plt.figure(figsize=(10, 7))
ax = plt.gca()

ax.set_facecolor("#ecf2f5")

ax.set_axisbelow(True)

plt.grid(True, which='both', color='lightgray', linestyle='-', linewidth=0.5)


ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

# plot the data
plt.scatter(N_exp, Z_exp, color='black', s=3, marker='s', label='Núcleos estables (experimentales)')  
plt.scatter(N_theo, Z_theo, color='darkorange', edgecolor='none', s=5, marker='s', label='Núcleos estables (teóricos)')

# Plot the line Z = N 
max_val = max(N_theo.max(), N_exp.max(), Z_theo.max(), Z_exp.max())
plt.plot(range(int(max_val)+1), range(int(max_val)+1), color='palevioletred', label='$Z = N$')


plt.xlim(0, 186)  
plt.ylim(0, 110) 

plt.xlabel('$N$', fontsize=14, family='serif')
plt.ylabel('$Z$', fontsize=14, family='serif')


plt.legend(loc='lower right', fontsize=14, framealpha=1, facecolor='white')


plt.tight_layout()
plt.savefig('ZvsN.png', dpi=300)
plt.show()