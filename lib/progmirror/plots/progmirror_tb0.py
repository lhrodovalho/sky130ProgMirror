import numpy as np
import matplotlib.pyplot as plt

###
data = np.loadtxt("../data/progmirror_tb0.csv", delimiter=",", skiprows=0)

vo = data[:, 0]
io = data[:, 1]*1e6

plt.figure(1)
plt.plot(vo,io,'-r')
plt.axis([0, 3.3, 0.6, 1.2])
plt.xticks([0,1,2,3,3.3])
plt.yticks([0.6,0.8,1.0,1.2])
plt.xlabel('Output voltage (V)')
plt.ylabel('Output current (uA)')
#plt.legend(loc="upper left")
plt.grid()
plt.draw()
plt.savefig("./progmirror_tb0.png")
#plt.clf()


plt.show()

###

