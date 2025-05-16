import numpy as np
import csv

# Coeficient values (MeV/c**2).
a_A = 92.88  
a_C = 0.71  


# Function to compute the relation between Z and N, (A = Z + N).
def Z(A):
    return (a_A * A**(4/3))/(2 * (A*a_C + A**(1/3)*a_A))


stable = []      # list where I will save the data of the stable nuclei


for A in range(2, 300):             # For different values of A = Z + N,
    Z_result = Z(A)                 # compute the function Z        
    Z_rounded = round(Z_result)     # round the result, for Z is an integer,
    N = A - Z_rounded               # calculate N.
    
    # since I want 1 <= Z <= 110, let me verify 
    if 1 <= Z_rounded <= 110 and N > 0:             # if Z is within the limits, and N is positive,
        stable.append((N, Z_rounded))               # I save them values into the list.


stable_nuclei = sorted(list(set(stable)))   # 'set' to eliminate duplicates,
                                            # 'list' to return the array into a list,
                                            # 'sorted' to put the values in ascendent order.


# to save in a cvs archive
with open('stablenuclei.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["N", "Z"])
    writer.writerows(stable_nuclei)
