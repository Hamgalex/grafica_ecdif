import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def returns_dydx(y,x):
    dydx = x-6
    return dydx
y0 = 1

x = np.linspace(-30,30)

y = odeint(returns_dydx, y0, x)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
