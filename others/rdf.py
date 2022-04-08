import numpy as np
import matplotlib.pyplot as plt

dimens=[3,3]
temp=[i for i in range(210,270,10)]+[273,285,300]
for k in range(dimens[0]):
    for j in range(dimens[1]):
        x=np.loadtxt("rdf_"+str(temp[dimens[1]*k+j])+"K.xvg",skiprows=25)
        plt.plot(x[:,0],x[:,1],label=str(temp[dimens[1]*k+j])+"K")
        #plt.title("Radial Distribution Function")
        plt.xlabel("r in n.m.")
        plt.ylabel("RDF")
plt.legend()
plt.show()

