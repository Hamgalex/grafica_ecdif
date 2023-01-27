import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def dSdx(S,x):
    y1, y2 = S
    return [y1 + y2**2  + 3*x,
           3*y1 + y2**3 - np.cos(x)]
           
S0=[0,0]

x = np.linspace(0, 1)
sol = odeint(dSdx, S0,x)

y1_sol = sol.T[0]
y2_sol = sol.T[1]


plt.plot(x, y1_sol)
plt.plot(x, y2_sol)

plt.show()