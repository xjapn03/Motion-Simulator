# Importar librerías necesarias
import numpy as np  # Para realizar cálculos matemáticos y manipular arrays
import matplotlib.pyplot as plt  # Para crear gráficos estáticos
import matplotlib.animation as animation  # Para crear animaciones en gráficos

# Definir la función de posición
def posicion(t):
    return 3*t**2 + 2*t + 1  # Función que devuelve la posición del objeto en función del tiempo t

# Crear la figura y el eje para la animación
fig, ax = plt.subplots()  # Crear una figura y un conjunto de ejes para la gráfica
ax.set_xlim(0, 10)  # Limitar el eje X (tiempo) entre 0 y 10
ax.set_ylim(0, 300)  # Limitar el eje Y (posición) entre 0 y 300

# Crear la línea vacía para la animación
line, = ax.plot([], [], lw=2)  # Crear un objeto de línea vacío, donde se dibujará la animación

# Función de inicialización (se llama al principio de la animación)
def init():
    line.set_data([], [])  # Inicializa la línea sin datos, empieza vacía
    return line,  # Devuelve la línea para la animación (como un "tuple" para compatibilidad con `FuncAnimation`)

# Función de animación (se llama para cada fotograma, 'i' es el número de fotograma actual)
def animate(i):
    t = np.linspace(0, 10, 100)  # Crear 100 valores de tiempo entre 0 y 10
    x = posicion(t)  # Calcular la posición del objeto para cada valor de tiempo usando la función definida
    line.set_data(t[:i], x[:i])  # Actualiza los datos de la línea: solo muestra los primeros 'i' puntos de la animación
    return line,  # Devuelve la línea actualizada para la animación

# Crear la animación
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True, interval=50)  
# FuncAnimation crea la animación, donde:
# - `fig` es la figura donde se dibuja
# - `animate` es la función que se llama para cada fotograma
# - `frames=100` indica cuántos fotogramas tendrá la animación
# - `init_func=init` es la función que se llama para inicializar la animación
# - `blit=True` optimiza el redibujado de la imagen solo cuando cambia (para eficiencia)
# - `interval=50` es el tiempo (en milisegundos) entre cada fotograma

# Mostrar la animación
plt.title('Movimiento del Objeto')  # Título de la gráfica
plt.xlabel('Tiempo (t)')  # Etiqueta del eje X (tiempo)
plt.ylabel('Posición (x)')  # Etiqueta del eje Y (posición)
plt.grid(True)  # Mostrar una cuadrícula en la gráfica
plt.show()  # Mostrar la gráfica interactiva con la animación
