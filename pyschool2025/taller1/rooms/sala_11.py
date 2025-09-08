from helpers import text, hyperlink

def revisar(respuesta):

    palabras_unidas = unir_palabras(["Misión", "PySchool 2025", "progreso a mitad", "con pequeñas dificultades", "pronto", "nuevo", "reporte"])

    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == palabras_unidas:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_12.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def unir_palabras(palabras):
    palabras_unidas = " ".join(palabras)
    return palabras_unidas

if __name__ == "__main__":
    palabras= ["Misión", "PySchool 2025", "progreso a mitad", "con pequeñas dificultades", "pronto", "nuevo", "reporte"]
    palabras_unidas = " ".join(palabras)

    revisar(None)
    revisar(palabras_unidas)
    revisar(False)
