import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as mda
from math import*

u=mda.Universe("../prod.gro","../md.xtc")
trj=u.trajectory

start=1
dt=14454
stop=len(trj)-dt

r,r_2=[],[]
for i in range(start,stop):
    trj[i].frame
    initial_frame=u.atoms[[0]].positions
    trj[i+dt].frame
    final_frame=u.atoms[[0]].positions
    d=np.sum((final_frame-initial_frame)**2)
    d_sqrt=d**0.5
    r.append(d_sqrt)
    r_2.append(d)
#**********************************************************************************
cutoff=str(input("\033[1;36;36m Set cutoff yes/no \n"))
if cutoff=='yes':
    for i in range(len(r)):
        if r[i]>10:
            r[i]=10
        if r_2[i]>10:
            r_2[i]=10
#**********************************************************************************
r2m=np.mean(r_2)
G=[]
C1=(3/(2*3.14*r2m))**1.5
C2=-3/(2*r2m)
for i in r:
    G.append(4*3.14*(i**2)*C1*exp(C2*(i**2)))

check_bins=str(input("\033[1;36;36m Do you want bin analysis yes/no \n"))
if check_bins=="yes":
    fig,axs=plt.subplots(3,3)
    for k in range(3):
        for j in range(3):
            axs[k][j].hist(r,50*(3*k+j+1),density=True)

plt.plot(r,G,"bo",label="G_{theo.}")
plt.hist(r,50,density=True,label="G_{exp.}")
plt.title("Van-Hove correlation function (T=200K)")
plt.xlabel("distance (in $\AA$)")
plt.ylabel("4$\pi$$r^2$G(r,t)")
plt.legend()
plt.show()
