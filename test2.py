import numpy as np
import matplotlib.pyplot as plt
x=[[0,0],[-35,5]]
y=[[-1,4],[0,0]]
v=[2,1.5,1,0.8,0.7,0.6,0.5,0.4,0.3,0.15,0.1,0,-5,-10,-15,-20,-30]
i=[3.866,2.551,1.215,0.524,0.475,0.263,0.036,0.006,0,0,0,0,0,0,0,0,0]
plt.figure(figsize=(8,6))
plt.ylabel('mA')
plt.xlabel('V')
plt.grid(True)
plt.plot(x[0],y[0],color='black')
plt.plot(x[1],y[1],color='black')
plt.plot(v, i, color='blue')
plt.show()
