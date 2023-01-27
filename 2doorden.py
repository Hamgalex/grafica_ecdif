import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def dP_dx(P,x):
    return [P[1],-P[1]**2+np.sin(x)]

P0=[0,5]

xs=np.linspace(0,1)
Ps=odeint(dP_dx,P0,xs)

print(Ps)

ys1=Ps[:,0]
ys2=Ps[:,1]


print("xd")

plt.plot(xs,ys1,color="red")

plt.plot(xs,ys2,color="blue")
plt.show()