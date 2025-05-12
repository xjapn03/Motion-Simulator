# Motion Simulator - Cálculo 1

Una aplicación web interactiva desarrollada con **Python**, **Streamlit** y **SymPy** para visualizar y analizar el movimiento de un objeto en función del tiempo: **posición**, **velocidad** y **aceleración**. Ideal para estudiantes de física o cálculo diferencial.

## Funcionalidades

- Selección de funciones predefinidas de movimiento:
  - Movimiento rectilíneo uniforme
  - Movimiento uniformemente acelerado
  - Movimiento oscilatorio
  - Movimiento polinómico complejo
- Permite escribir funciones personalizadas `x(t)` en notación matemática de Python
- Visualización dinámica de:
  - Posición `x(t)`
  - Velocidad `v(t)` (derivada de `x(t)`)
  - Aceleración `a(t)` (derivada de `v(t)`)
- Control del rango de tiempo con sliders

## Tecnologías

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [SymPy](https://www.sympy.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/) (para gráficos animados en otra vista)

## Instalación local

1. Clona el repositorio:

   ```bash
   git clone https://github.com/xjapn03/Motion-Simulator.git
   cd Motion-Simulator

2. (Opcional) Crea un entorno virtual:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt

4. Ejecuta la aplicación:

    ```bash
    streamlit run app.py