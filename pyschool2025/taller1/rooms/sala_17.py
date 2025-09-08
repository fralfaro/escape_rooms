from helpers import text, hyperlink

def revisar(respuesta):
    codigo_salida = 963

    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == codigo_salida:
        hyperlink("¡Correcto! Haz click aquí para despegar de vuelta a la Tierra", "sala_final.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def es_primo(numero):

    if numero <= 3: return True
    else:
        for i in range(2, numero - 1):
            if numero % i == 0: return False
        return True

def suma_numeros_primos(codigo_secreto):
    suma = 0
    numero = 2
    contador = 0
    for _ in range(1, 1000):
        if es_primo(numero):
            suma += numero
            contador += 1
        numero += 1
        if contador == codigo_secreto: break
    return suma

if __name__ == "__main__":
    revisar(None)
    revisar(suma_numeros_primos(24))
    revisar(False)
