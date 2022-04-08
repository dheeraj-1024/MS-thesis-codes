import numpy as np
import matplotlib.pyplot as plt

temp=[i for i in range(200,270,10)]+[273,285,300]
avg_by=int(input("take avg. over = "))

fig,axs=plt.subplots(3,3)
for k in range(3):
    for j in range(3):
        x=np.loadtxt("data_msd_1_"+str(temp[3*k+j])+"K.dat")
        list_1=[np.mean(x[1][i:i+avg_by]) for i in range(len(x[1]))]
        axs[k][j].plot(x[0],x[1],"bo")
        axs[k][j].plot(x[0],list_1,"go")
        axs[k][j].set_title(str(temp[3*k+j])+"K")
fig.suptitle("Non-Gaussian Parameter vs time")
plt.show()

