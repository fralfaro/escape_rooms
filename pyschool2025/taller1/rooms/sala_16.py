from helpers import text, hyperlink

def revisar(respuesta):

    grados = ['muy bajo', 'bajo', 'alto', 'bajo', 'medio']

    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == grados:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_17.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def niveles_temperatura(temperaturas):
    niveles_corregidos = []
    for temperatura in temperaturas:
        fahrenheit = a_fahrenheit(temperatura)

        if fahrenheit <= 28.400:
            niveles_corregidos.append('muy bajo')

        elif 28.400 < fahrenheit <= 53.600:
            niveles_corregidos.append('bajo')

        elif  53.600 < fahrenheit <= 64.400:
            niveles_corregidos.append('medio')

        elif fahrenheit > 64.400:
            niveles_corregidos.append('alto')

    return niveles_corregidos



if __name__ == "__main__":
    temperaturas = [-2, 0, 25, -1, 16]
    revisar(None)
    revisar(niveles_temperatura(temperaturas))
    revisar(False)
