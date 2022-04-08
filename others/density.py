import numpy as np
import matplotlib.pyplot as plt
from math import*

x=np.loadtxt("density.dat",skiprows=1)
plt.plot(x[:,1],x[:,2],"b-",label="Simulation data")
plt.plot(x[:,3],x[:,4],"g-",label="Experimental data")
plt.plot(x[:,1],x[:,2],"bo")
plt.plot(x[:,3],x[:,4],"go")
plt.title("Density vs Temperature")
plt.ylabel("Density $(kg/m^3)$")
plt.xlabel("Temperature $(K)$")
plt.legend()
plt.show()
