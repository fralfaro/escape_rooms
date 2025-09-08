from helpers import text, hyperlink

def revisar(respuesta):

    lista = [(20, 30), (21, 29), (22, 28), (23, 27), (24, 26), (25, 25), (26, 24), (27, 23), (28, 22), (29, 21), (30, 20)]
    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == lista:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_16.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")


def combinaciones():
    coordenadas = list(range(1, 31))
    combinaciones_validas = []

    for x in coordenadas:
        for y in coordenadas:
            if x + y == 50:
                combinaciones_validas.append((x, y))

    return combinaciones_validas


if __name__ == "__main__":
    revisar(None)
    revisar(combinaciones())
    revisar(False)
