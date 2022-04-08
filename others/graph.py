import numpy as np
import matplotlib.pyplot as plt
from math import*

temp=str(input("Enter temperature = "))
data=np.loadtxt("data_msd_1_"+temp+"K.dat")
x=data[0]
y=data[1]
avg_by=int(input("take avg. over = "))
list_1=[np.mean(y[i:i+avg_by]) for i in range(len(y))]
print(np.shape(x))
plt.plot(x,y,label="raw data")
plt.plot(x,list_1,label="running average("+str(avg_by)+")")
plt.legend()

plt.title("NGP vs time (T="+temp+"K)")
plt.xlabel("time in ps")
plt.ylabel("Non-gaussian parameter $\\alpha_2(t)$")
plt.show()
