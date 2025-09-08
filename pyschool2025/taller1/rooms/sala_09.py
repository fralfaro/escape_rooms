from helpers import text, hyperlink

def revisar(respuesta):

    lista = ['linterna', 'monitor principal', 'antena', 'filtro gases', 'lentes infrarojo', 'teclado']
    if respuesta == lista:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_10.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    lista = ['linterna', 'monitor principal', 'antena', 'filtro gases', 'lentes infrarojo', 'teclado']
    revisar(None)
    revisar("lista")
    revisar(lista)
