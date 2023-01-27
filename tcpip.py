import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a=1
b=1/2
T=5

def returns_dydx(y,x):
    dydx = a-(a+(2*b*x)/(2-b))*1/T
    return dydx

x = np.linspace(0,10)
y0=2

y = odeint(returns_dydx, y0, x)
  
plt.plot(x,y)
plt.xlabel("t")
plt.ylabel("x")
plt.show()