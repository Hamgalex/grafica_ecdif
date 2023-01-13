
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
  
def returns_dydt(y,t):
    dydt = 6 -t
    return dydt
  
# Condición inicial
y0 = 1
  
# Rango de t
t = np.linspace(-60,80)
  
# resolver la ecdif
y = odeint(returns_dydt, y0, t)
  
# Graficar los resultados
plt.plot(t,y)
plt.xlabel("Tiempo")
plt.ylabel("Y")
plt.show()