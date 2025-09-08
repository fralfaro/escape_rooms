from helpers import text, hyperlink

def revisar(respuesta):

    mensaje = "el codigo secreto que se debe ocupar en el ultimo desafio es 24"

    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == mensaje:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_15.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")


def mensaje_decodificado(mensaje):
    diccionario = {
        '._': 'a', '_...': 'b', '_._.': 'c', '_..': 'd',
        '.': 'e', '.._.': 'f', '__.': 'g', '....': 'h',
        '..': 'i', '.___': 'j', '_._': 'k', '._..': 'l',
        '__': 'm', '_.': 'n', '___': 'o', '.__.': 'p',
        '__._': 'q', '._.': 'r', '...': 's', '_': 't',
        '.._': 'u', '..._': 'v', '.__': 'w', '_.._': 'x',
        '_.__': 'y', '__..': 'z', '__._.': ' ', '_____': '0',
        '.____': '1', '..___': '2', '...__': '3', '...._': '4',
        '.....': '5', '_....': '6', '__...': '7', '___..': '8',
        '____.': '9'
    }

    decodificado = [diccionario[simbolo] for simbolo in mensaje]
    return ''.join(decodificado)

if __name__ == "__main__":
    mensaje = [
        '.', '._..', '__._.',  # e l
        '_._.', '___', '_..', '..', '__.', '___', '__._.', # c o d i g o
        '...', '.', '_._.', '._.', '.', '_', '___', '__._.', # s e c r e t o
        '__._', '.._', '.', '__._.',  # q u e
        '...', '.', '__._.', # s e
        '_..', '.', '_...', '.', '__._.', # d e b e
        '___', '_._.', '.._', '.__.', '._', '._.', '__._.', # o c u p a r
        '.', '_.', '__._.', # e n
        '.', '._..', '__._.', # e l
        '.._', '._..', '_', '..', '__', '___', '__._.', # u l t i m o
        '_..', '.', '...', '._', '.._.', '..', '___', '__._.', # d e s a f i o
        '.', '...', '__._.', # e s
        '..___', '...._'  # 2 4
    ]

    revisar(None)
    revisar(mensaje_decodificado(mensaje))
    revisar(True)