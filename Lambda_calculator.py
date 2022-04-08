""" This program is used to calculate distance travelled by molecules. """
import MDAnalysis as mda                                             #     ________________________
import numpy as np                                                   #     |  importing modules   |
import matplotlib.pyplot as plt                                      #     ------------------------
from math import*                                                    #  

str_1=str(input("Enter structure filename = "))                      #     _________________________
str_2=str(input("\nEnter trajectory filename = "))                   #     |   taking user inputs  |
dummy_t=int(input("\nEnter frames = "))                              #     -------------------------
temp=str(input("Enter temperature = "))                              #

print("structure taken was = ",str_1," trajectory file taken = ",str_2,"dummy_t = ",dummy_t)
u=mda.Universe(str_1,str_2)
trj=u.trajectory

#********************************************************************************************
def r_cm_giver(fr):
    n=np.shape(fr)[0]                                                            #    defination for calculation of center of mass
    a=[]
    for i in range(1000):
        b=[]
        for j in range(3):
            sumn=0
            for k in  range(n):
                sumn+=fr[k][i][j]
            b+=[sumn]
        a+=[b]
    outp=np.array(a)
    return outp/n
#********************************************************************************************
def modular_r_giver(l,t_start,t_stop):
    diff_array_2=[]
    for i in range(t_start,t_stop):
        frame = trj[i].frame
        pos = u.atoms[[i for i in range(0,5000,5)]].positions
        diff = pos-l
        mod_diff=[]
        for j in range(1000):
            mod_diff+=[diff[j][0]+diff[j][1]+diff[j][2]]
        mod_diff_array=np.array(mod_diff)
        diff_array_2+=[mod_diff_array**2]
    outp=np.array(diff_array_2)
    return outp
#********************************************************************************************
def Rg_giver(modular_r):
    answer=[]                                                                        #        defination for calculation of radius of gyration.
    n=np.shape(modular_r)[0]
    for i in range(np.shape(modular_r)[1]):
        sumn=0
        for j in range(n):
            sumn+=modular_r[j][i]
        answer+=[sumn]
    answer_array=np.array(answer)
    new=answer_array/n
    outp=np.sqrt(new)
    return outp
#********************************************************************************************

t_star=dummy_t
n=t_star
start_frame=1
stop_frame=len(trj)-n
r_cm=[]

for i in range(start_frame,stop_frame,t_star):
    frames=[]
    for j in range(i,i+t_star):
        frame_j=trj[j].frame
        position_j=u.atoms[[i for i in range(0,5000,5)]].positions
        frames+=[position_j]
    r_cm+=[r_cm_giver(np.array(frames))]
r_cm_array=np.array(r_cm)

#                                           /--------------------------------------------------------------------------------\
#                                           |r_cm_array is an array of positions of center of mass for i=1,2,3.... iterations|
#                                           \--------------------------------------------------------------------------------/

R=[]
for i in range(np.shape(r_cm_array)[0]):
    mod_r=modular_r_giver(r_cm_array[i],(i*t_star)+1,(i+1)*t_star)
    R+=[Rg_giver(mod_r)]
Rg=np.array(R)
lambDa=2*Rg.mean(1)
print(lambDa)                               #distance travelled by particles in i-th time interval
np.savetxt("dist_1_"+temp+".dat",lambDa)



