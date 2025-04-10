import streamlit as st
from streamlit_lottie import st_lottie
import json
import time


# Función para cargar animaciones locales
def load_lottiefile(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


# Configuración inicial de Streamlit
st.set_page_config(page_title="Escape Room PySchool", layout="centered")

st.title("🚪 Escape Room: PySchool Edition")

# Inicializar estados
if "sala_actual" not in st.session_state:
    st.session_state.sala_actual = 0

if "desafio_superado" not in st.session_state:
    st.session_state.desafio_superado = False

if "mostrar_puerta" not in st.session_state:
    st.session_state.mostrar_puerta = False


# Cargar animaciones
lottie_success = load_lottiefile("animations/success.json")
lottie_puzzle = load_lottiefile("animations/puzzle.json")
lottie_wrong = load_lottiefile("animations/wrong.json")
lottie_puerta = load_lottiefile("animations/puerta.json")


# Mostrar solo animación de la puerta y avanzar
def pantalla_puerta():
    contenedor = st.empty()  # Reservar espacio vacío
    with contenedor:
        st_lottie(lottie_puerta, height=400)
    time.sleep(2)
    st.session_state.sala_actual += 1
    st.session_state.desafio_superado = False
    st.session_state.mostrar_puerta = False
    st.rerun()


# Mensaje para pasar de sala (botón que activa animación de puerta)
def mensaje_avanzar():
    st_lottie(lottie_success, height=250)
    st.success("🎉 ¡Muy bien! Puedes avanzar a la siguiente habitación.")
    if st.button("👉 Avanzar a la siguiente sala"):
        st.session_state.mostrar_puerta = True
        st.rerun()


# Lógica de cada sala
def mostrar_sala(num):
    #st_lottie(lottie_puzzle, height=250)

    if num == 0:
        st.subheader("🔎 Sala 0: La Clave Secreta")
        respuesta = st.text_input("¿Cuál es la palabra mágica?")
        if st.button("Verificar"):
            if respuesta == "PySchool2025":
                st.session_state.desafio_superado = True
            else:
                st_lottie(lottie_wrong, height=200)
                st.warning("Ups... esa no es la clave correcta.")

    elif num == 1:
        st.subheader("💬 Sala 1: Tradición Programadora")
        respuesta = st.text_input("¿Qué se escribe primero al aprender a programar?")
        if st.button("Verificar"):
            if respuesta == "Hola Mundo":
                st.session_state.desafio_superado = True
            else:
                st_lottie(lottie_wrong, height=200)
                st.warning("No es correcto. ¡Recuerda las clases!")

    elif num == 2:
        st.subheader("🧠 Sala 2: Desafío Matemático Final")
        st.latex(r"\frac{1.23 + 2.34}{1 + \frac{43}{2}} + 3 \times 2^{1.5}")
        respuesta = st.number_input("Ingresa tu resultado:", step=0.01)
        resultado_correcto = (1.23 + 2.34) / (1 + 43/2) + 3 * 2**1.5
        if st.button("Verificar"):
            if abs(respuesta - resultado_correcto) < 1:
                st.session_state.desafio_superado = True
            else:
                st_lottie(lottie_wrong, height=200)
                st.warning("Prueba de nuevo con más precisión.")

    elif num == 3:
        st.balloons()
        st.success("🎉 ¡Has escapado exitosamente del Escape Room!")
        if st.button("🔁 Reiniciar juego"):
            st.session_state.sala_actual = 0
            st.session_state.desafio_superado = False
            st.session_state.mostrar_puerta = False
            st.rerun()

    if st.session_state.desafio_superado and num < 3:
        mensaje_avanzar()


# Mostrar la pantalla correcta
if st.session_state.mostrar_puerta:
    pantalla_puerta()
else:
    mostrar_sala(st.session_state.sala_actual)
