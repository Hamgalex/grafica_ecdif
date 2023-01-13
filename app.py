
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

print("Escriba la ecuación diferencial")
expression=input("dydt=")

print("escriba la condicion inicial")
y0=input("y0=")

def returns_dydt(y,t):
    dydt = eval(expression)
    return dydt
  
# Rango de t
t = np.linspace(0,5)
  
# resolver la ecdif
y = odeint(returns_dydt, y0, t)
  
# Graficar los resultados
plt.plot(t,y)
plt.xlabel("Tiempo")
plt.ylabel("Y")
plt.show()