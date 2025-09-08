from helpers import text, hyperlink

def revisar(func):

    try:
        escila = func("asteroide esciLa")
        sofrosina = func("sofrosina asteroide")
        aarhus = func("aarhus meteorito")
        andura = func("andura meteorito")

        if escila == "ASTEROIDE ESCILA" and sofrosina == "SOFROSINA ASTEROIDE" and aarhus == "aarhus meteorito" and andura == "andura meteorito":
            hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_11.html", "success")
        else:
            text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

    except Exception as e:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")



def desafio(palabra):

    if "asteroide" in palabra: palabra = palabra.upper()
    elif "meteorito" in palabra: palabra = palabra.lower()

    return palabra

if __name__ == "__main__":
    revisar(None)
    revisar(desafio)
    revisar(False)
