import numpy as np
import matplotlib.pyplot as plt

x,y=[],[]
for i in range(20000,720000,20000):
    if i == 520000:
        continue
    data=np.loadtxt("entropy_"+str(i)+".dat",skiprows=2)
    x.append(i/1000)
    y.append(np.mean(data[:,1]))

plt.plot(x,y,"bo")
plt.plot(x,y)
plt.xlabel("time (in ns)")
plt.ylabel("$SWE_{avg}$")
plt.show()
