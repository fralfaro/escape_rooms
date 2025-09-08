from helpers import text, hyperlink

def revisar(respuesta):

    diccionario = {'PS004': 80, 'PS014': 120, 'PS104': 50}

    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == diccionario:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_13.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")


if __name__ == "__main__":
    revisar(None)
    revisar(True)
    revisar(False)
