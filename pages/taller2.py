import streamlit as st
from streamlit_lottie import st_lottie
import json
import time


# Cargar animaciones
def load_lottiefile(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_success = load_lottiefile("animations/success.json")
lottie_wrong = load_lottiefile("animations/wrong.json")
lottie_puerta = load_lottiefile("animations/puerta.json")


# config
SALAS = {
    0: {
        "titulo": "🔎 Sala 0: La Clave Secreta",
        "func_situacion": "sala_0_situacion",
        "pregunta": "¿Cuál es la palabra mágica?",
        "respuesta_correcta": "PySchool2025",
        "pistas": [
            "Busca en el nombre del evento y el año actual.",
            "Revisa las primeras letras de cada palabra.",
            "Solución: PySchool2025"
        ],
        "tipo": "texto"
    },
    1: {
        "titulo": "💬 Sala 1: Tradición Programadora",
        "func_situacion": "sala_1_situacion",
        "pregunta": "¿Qué se escribe primero al aprender a programar?",
        "respuesta_correcta": "Hola Mundo",
        "pistas": [
            "Es una frase clásica que aparece en tu primer programa.",
            "En Python lo escribirías con print('...?')",
            "Solución: Hola Mundo"
        ],
        "tipo": "texto"
    },
    2: {
        "titulo": "🧠 Sala 2: Desafío Matemático Final",
        "func_situacion": "sala_2_situacion",
        "pregunta": r"\frac{1.23 + 2.34}{1 + \frac{43}{2}} + 3 \times 2^{1.5}",
        "respuesta_correcta": 8,  # Puedes poner el número más preciso si quieres
        "pistas": [
            "Suma primero los números del numerador.",
            "Recuerda las prioridades de operaciones y potencias.",
            "Solución: Aproximadamente 8"
        ],
        "tipo": "numero"
    }
}


# salas
def sala_0_situacion():
    st.write("Te encuentras en una sala misteriosa con un cofre cerrado...")
    #st.image("img/cofre.png")

def sala_1_situacion():
    st.write("Encuentras un computador antiguo...")
    st.code('print("Hola Mundo")', language='python')

def sala_2_situacion():
    st.write("Debes resolver un problema matemático para escapar.")
    #st.image("img/matematica.png")

def mostrar_sala_final():
    st.balloons()
    st.success("🎉 ¡Has escapado exitosamente del Escape Room!")
    if st.button("🔁 Reiniciar juego"):
        st.session_state.sala_actual = 0
        st.session_state.desafio_superado = False
        st.session_state.mostrar_puerta = False
        st.rerun()




# Config inicial
st.set_page_config(page_title="Escape Room PySchool", layout="centered", initial_sidebar_state="collapsed")

st.title("🚪 Escape Room: PySchool Edition")

# Estados iniciales
if "sala_actual" not in st.session_state:
    st.session_state.sala_actual = 0
if "desafio_superado" not in st.session_state:
    st.session_state.desafio_superado = False
if "mostrar_puerta" not in st.session_state:
    st.session_state.mostrar_puerta = False

# Mostrar animación de puerta
def pantalla_puerta():
    cont = st.empty()
    with cont:
        st_lottie(lottie_puerta, height=400)
    time.sleep(2)
    st.session_state.sala_actual += 1
    st.session_state.desafio_superado = False
    st.session_state.mostrar_puerta = False
    st.rerun()

# Mensaje éxito
def mensaje_avanzar():
    st_lottie(lottie_success, height=250)
    st.success("🎉 ¡Muy bien! Puedes avanzar a la siguiente habitación.")
    if st.button("👉 Avanzar a la siguiente sala"):
        st.session_state.mostrar_puerta = True
        st.rerun()

# Mostrar Sala Dinámica
def mostrar_sala(num):
    if num == len(SALAS):
        mostrar_sala_final()
        return

    sala = SALAS[num]
    tabs = st.tabs(["🕵️ Situación", "❓ Acertijo", "💡 Pistas"])


    with tabs[0]:
        st.subheader(sala["titulo"])
        globals()[sala["func_situacion"]]()  # Ejecutar función personalizada

    with tabs[1]:
        if sala["tipo"] == "texto":
            respuesta = st.text_input(sala["pregunta"])
        else:
            st.latex(sala["pregunta"])
            respuesta = st.number_input("Ingresa tu resultado:", step=0.01)

        if st.button("Verificar"):
            correcto = sala["respuesta_correcta"]
            if sala["tipo"] == "texto":
                if respuesta == correcto:
                    st.session_state.desafio_superado = True
                else:
                    st_lottie(lottie_wrong, height=200)
                    st.warning("Respuesta incorrecta.")
            else:
                if abs(respuesta - correcto) < 1:
                    st.session_state.desafio_superado = True
                else:
                    st_lottie(lottie_wrong, height=200)
                    st.warning("Respuesta incorrecta.")

    with tabs[2]:
        st.subheader("💡 Pistas")
        for i, pista in enumerate(sala["pistas"], start=1):
            with st.expander(f"Pista {i}"):
                st.write(pista)

    if st.session_state.desafio_superado:
        mensaje_avanzar()

# Render
if st.session_state.mostrar_puerta:
    pantalla_puerta()
else:
    mostrar_sala(st.session_state.sala_actual)

css = '''
    <style>
        /* Adjust the text size in the Tabs */
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.5rem; /* Text size in the tabs */
        }

        /* Additional option: Adjust the header size within expanders */
        .st-expander h1, .st-expander h2, .st-expander h3 {
            font-size: 4rem; /* Header size within expanders */
        }

        /* Adjust the text size of the selectbox in the sidebar */
        .sidebar .stSelectbox label {
            font-size: 1.5rem; /* Adjust this value to change the text size */
        }

    </style>
    '''

st.markdown(css, unsafe_allow_html=True)