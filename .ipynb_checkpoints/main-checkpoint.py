import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Función de posición en el tiempo (ejemplo)
t = sp.Symbol('t')
x = 3*t**2 + 2*t + 1  # Esta es la posición

# Mostrar la función de posición
x


# Derivada para obtener la velocidad
v = sp.diff(x, t)

# Derivada de la velocidad para obtener la aceleración
a = sp.diff(v, t)

v, a


# Graficar la posición con matplotlib
t_vals = np.linspace(0, 10, 100)
x_vals = 3*t_vals**2 + 2*t_vals + 1

plt.plot(t_vals, x_vals)
plt.title('Posición del objeto')
plt.xlabel('Tiempo (t)')
plt.ylabel('Posición (x)')
plt.grid(True)
plt.show()


import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 300)

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    t = np.linspace(0, 10, 100)
    x = 3*t**2 + 2*t + 1
    line.set_data(t[:i], x[:i])
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)
plt.show()
