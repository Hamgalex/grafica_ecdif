
# Ejemplo 1: 1erorden.py [https://github.com/Hamgalex/grafica_ecdif/blob/master/1erorden.py] 
Se resuelve la siguiente ecuación diferencial:
$$\frac{dy}{dx}=x-6$$ donde $$y(0)=1$$

## Ejemplo 2: 1erordenacoplada.py [https://github.com/Hamgalex/grafica_ecdif/blob/master/1erordenacoplada.py] 
Se resuelve la siguiente ecuación diferencial:
$$y_1' = y_1 + y_2^2 + 3x, \text{ con  } y_1(0)=0$$
$$y_2' = 3y_1 + y_2^3 - \cos(x), \text{ con  } y_2(0)=0$$

## Ejemplo 3: 2doorden.py [https://github.com/Hamgalex/grafica_ecdif/blob/master/2doorden.py] 
Se resuelve la siguiente ecuación diferencial:
$$\ddot{x} = -\dot{x}^2 + \sin(x)$$ donde $$x_0=0 \text{ y }  v_0=5$$



## Ejemplo 4: 3erordenacoplada.py [https://github.com/Hamgalex/grafica_ecdif/blob/master/3erordenacoplada.py] 
Se resuelve la siguiente ecuación diferencial:
$$\dddot{x_2}= -\ddot{x_1}^3 + \dot{x_2} + x_1 + \sin(t)$$
$$\dddot{x_1}= -2\dot{x_2}^2 + x_2$$
con todas las condiciones iniciales en cero.

## Ejemplo 5: tcpip.py [https://github.com/Hamgalex/grafica_ecdif/blob/master/tcpip.py] 
Ejemplo del modelo TCP IP página 17 de control de sistemas no lineales editorial pearson
