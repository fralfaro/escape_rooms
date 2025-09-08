from helpers import text, hyperlink

def revisar(respuesta):
    lista = [150, 375, 890]

    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == lista:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_08.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def ordernar_coordenadas(coordenadas):
    coordenadas.sort()
    largo = len(coordenadas)

    valor_medio = (coordenadas[(largo//2) - 1] + coordenadas[largo//2]) //2 \
        if largo %2 == 0 \
        else coordenadas[largo//2]

    return [coordenadas[0],
            valor_medio,
            coordenadas[-1]]


if __name__ == "__main__":
    coordenadas = [540, 320, 890, 150, 430, 270]
    revisar("test")
    revisar(ordernar_coordenadas(coordenadas))
    revisar(None)
