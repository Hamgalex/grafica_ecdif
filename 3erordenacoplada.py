import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def dSdt(S,t):
    x1, v1, a1, x2, v2, a2 = S
    return [v1,
            a1,
            -2*v2**2 + x2,
            v2,
            a2,
            -a1**3 + v2 + v1 + np.sin(t)]
x1_0 = 0
v1_0 = 0
a1_0 = 0
x2_0 = 0
v2_0 = 0
a2_0 = 0
v_0 = 0
S_0 = [x1_0, v1_0, a1_0, x1_0, v1_0, a1_0]
t = np.linspace(0, 1)
sol = odeint(dSdt, S_0, t)
plt.plot(t,sol.T[0])

plt.show()