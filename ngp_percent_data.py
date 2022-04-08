"""Code to calculate non-gaussian parameter (NGP). """
import numpy as np                                          #           *********************
from math import*                                           #           * importing modules *
import MDAnalysis as mda                                    #           *********************
import matplotlib.pyplot as plt                             #
import random                                               #
import MDAnalysis.analysis.msd as msd

u=mda.Universe("../prod.gro","../md.xtc")
trj=u.trajectory

print("length of trajectory to be analysed is ",len(trj))
#number=float(input("Enter the fraction of data you want to consider for calculations = "))
number=.1
time,r_2=[],[]
r_4=[]
start=1
stop=len(trj)

for i in range(1,stop-start-1,100):
    d,d_4=[],[]
    for j in range(10):
        l=int(number*(stop-start-i)*j)
        trj[l].frame
        init_frame=u.atoms[[k for k in range(0,1000,5)]].positions
        trj[l+i].frame
        final_frame=u.atoms[[k for k in range(0,1000,5)]].positions
        d.append(np.sum((final_frame-init_frame)**2,1))
        d_4.append(np.sum((final_frame-init_frame)**4,1))
    r_2.append(np.mean(d,0))
    r_4.append(np.mean(d_4,0))
    time.append(log(i,10))
    print("\b"*18,'{0:.2f}'.format((i*100)/(stop-start)),"% completed",end = "",flush=True)

ngp=[]
for i in range(np.shape(r_2)[1]):
    ng=[]
    for j  in range(len(r_2)):
        fr=(3*r_4[j][i])/(5*(r_2[j][i]**2))
        ng.append(fr-1)
    ngp.append(ng)
ngp_avg=np.mean(ngp,0)
print(np.shape(ngp),np.shape(ngp_avg))

for i in range(np.shape(r_2)[1]):
    plt.plot(time,ngp[i])
plt.show()

data=[time,ngp_avg]
np.savetxt("ngp_1.dat",data)
plt.plot(time,ngp_avg)
plt.show()
