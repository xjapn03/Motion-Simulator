import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# diccionario simbolico
t = sp.Symbol('t')
locals_dict = {"t": t, "sin": sp.sin, "cos": sp.cos, "exp": sp.exp}

# funciones predefinidas
funciones_ejemplo = {
    "x(t) = 3t² + 2t + 1 (Movimiento uniformemente acelerado)": "3*t**2 + 2*t + 1",
    "x(t) = 5t + 10 (Movimiento rectilíneo uniforme)": "5*t + 10",
    "x(t) = 10*sin(t) (Movimiento oscilatorio)": "10*sin(t)",
    "x(t) = t³ - 6t² + 9t (Movimiento complejo)": "t**3 - 6*t**2 + 9*t"
}

st.title("🌟 Simulador Interactivo de Movimiento (Calculo 1)")

opcion = st.selectbox("Elige una función de ejemplo:", list(funciones_ejemplo.keys()))
funcion_default = funciones_ejemplo[opcion]

st.subheader("O escribe tu propia funcion x(t):")
funcion_usuario = st.text_input("Funcion de posicion x(t):", value=funcion_default)

# rango tiempo
st.sidebar.header("⏱️ Rango de Tiempo")
t0 = st.sidebar.slider("Inicio", 0.0, 10.0, 0.0)
t1 = st.sidebar.slider("Fin", t0, 20.0, 10.0)

# procesa funcion
try:
    # asegurarse de que la expresion tiene la variable 't'
    x_expr = sp.sympify(funcion_usuario, locals=locals_dict)
    if t not in x_expr.free_symbols:
        raise ValueError("La función debe depender de 't'")

    v_expr = sp.diff(x_expr, t)
    a_expr = sp.diff(v_expr, t)

    # convierte a funciones de numpy
    x_func = sp.lambdify(t, x_expr, modules=['numpy'])
    v_func = sp.lambdify(t, v_expr, modules=['numpy'])
    a_func = sp.lambdify(t, a_expr, modules=['numpy'])

    # tiempo y evaluaciones
    t_vals = np.linspace(t0, t1, 300)
    x_vals = np.array([x_func(ti) for ti in t_vals])
    v_vals = np.array([v_func(ti) for ti in t_vals])
    a_vals = np.array([a_func(ti) for ti in t_vals])



    # validacion, asegurar misma dimension
    if any(arr.shape != t_vals.shape for arr in [x_vals, v_vals, a_vals]):
        raise ValueError("La función no se evaluó correctamente sobre el rango de tiempo")

    # mostrar formulas
    st.subheader("📄 Expresiones Calculadas:")
    st.latex(f"x(t) = {sp.latex(x_expr)}")
    st.latex(f"v(t) = {sp.latex(v_expr)}")
    st.latex(f"a(t) = {sp.latex(a_expr)}")

    # Gráficas
    def graficar(t_vals, y_vals, label, color):
        fig, ax = plt.subplots()
        ax.plot(t_vals, y_vals, label=label, color=color)
        ax.set_xlabel("t")
        ax.set_ylabel(label)
        ax.grid(True)
        st.pyplot(fig)

    st.subheader("📈 Posición")
    graficar(t_vals, x_vals, "x(t)", "blue")

    st.subheader("📈 Velocidad")
    graficar(t_vals, v_vals, "v(t)", "orange")

    st.subheader("📈 Aceleración")
    graficar(t_vals, a_vals, "a(t)", "red")

except Exception as e:
    st.error("⚠️ Error al interpretar la función. Asegúrate de usar notación válida en Python (por ejemplo: t**2, sin(t), etc.)")
    st.code(str(e))