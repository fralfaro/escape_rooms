# types: warning, danger, success, info, primary

import statistics

########################################################
# UTILIDADES
########################################################

def text(text="", type="info"):
    text_str = f'<div class="btn btn-{type}" w-100 h-100>{text}</div>'
    print(text_str)


def hyperlink(text, url, type="info"):
    text_str = f'<a href="{url}" class="btn btn-{type} w-100 h-100">{text}</a>'
    print(text_str)


def autorizar_acceso(acceso, resistencia):

    # Escribe tu respuesta aquí
    if acceso == True and resistencia == "Alta":
        return True
    else:
        return False

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

########################################################
# SALONES
########################################################

def salon_0(answer):
    if answer == "PYTHON-25":
        hyperlink("¡Correcto! Avanza a la siguiente página", "1.html", "success")
    else:
        incorrect_answer = f"""Estás probando nuevas respuestas, muy bien.  
        Recuerda que la respuesta es PYTHON-25"""
        text(incorrect_answer, "warning")


def salon_1(answer):
    if answer == "Cerrar":
        hyperlink("¡Correcto! Avanza a la siguiente página", "2.html", "success")
    elif answer == None:
        text("Indica la solución asignando algún valor a la variable `respuesta`.", "info")
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")


def salon_2(answer):
    true_answer = ( (1.23 + 2.34) / (1 + (43 / 2) ) ) + (3 * 2**1.5)
    epsilon = 0.000001
    if type(answer) in [float, int] and abs(answer - true_answer) < epsilon:
        hyperlink("¡Correcto! Avanza a la siguiente página", "3.html", "success")
    elif answer == None:
        text("Indica la solución asignando algún valor a la variable `respuesta`.", "info")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def salon_3(respuesta):
    mean = statistics.mean([19.5, 22.3, 12, 10.01, 32, 29.99, 20.89])
    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == mean:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "4.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def salon_4(respuesta):
    lista = [150, 375, 890]

    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == lista:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "5.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def salon_5(autorizar_acceso):

    acceso_tripulante_uno = autorizar_acceso(True, "Alta")
    acceso_tripulante_dos = autorizar_acceso(True, "Baja")
    acceso_tripulante_tres = autorizar_acceso(False, "Alta")

    if acceso_tripulante_uno == True and acceso_tripulante_dos == False and acceso_tripulante_tres == False:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "6.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def salon_6(respuesta):
    suma = sum(range(1,1001))
    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == suma:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "7.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def salon_7(respuesta):
    diccionario = {'PS004': 80, 'PS014': 120, 'PS104': 50}

    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == diccionario:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "8.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def salon_8(respuesta):
    codigo_salida = 963

    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == codigo_salida:
        hyperlink("¡Correcto! Haz click aquí para despegar de vuelta a la Tierra", "end.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")



def salon_00(url, df):
    url_correcta = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'
    if url is None or df is None:
        text("Debes asignar un valor a las variables `url` y `df`.", "info")
    elif url == url_correcta and len(df.columns) >= 10:
        hyperlink("¡Correcto! Has restaurado el sistema del laboratorio. Avanza a la siguiente sala.", "1.html", "success")
    else:
        text("Revisa bien las instrucciones... ¿Estás seguro que cargaste los datos correctamente?", "warning")


def salon_11(desc):
    import pandas as pd

    if desc is None:
        text("Debes asignar valores a las variables `info` y `desc` ejecutando `df.info()` y `df.describe()`.", "info")
    
    elif not isinstance(desc, pd.DataFrame):
        text("La variable `desc` debe ser el resultado de `df.describe()`.", "warning")
    
    else:
        hyperlink("¡Perfecto! Has explorado correctamente el dataset. Avanza a la siguiente sala.", "2.html", "success")

def salon_22(respuesta):
    if respuesta is None:
        text("Debes asignar el número total de tipos de Pokémon a la variable `respuesta`.", "info")
    elif respuesta == [18, 'Water', 'Flying']:
        hyperlink("¡Correcto! Existen 18 tipos de Pokémon. Avanza a la siguiente sala.", "3.html", "success")
    else:
        text("La puerta sigue cerrada... Revisa bien los datos y cuenta nuevamente los tipos de Pokémon.", "warning")

def salon_33(respuesta_ataque, respuesta_defensa):
    if respuesta_ataque is None or respuesta_defensa is None:
        text("Debes definir las variables `respuesta_ataque` y `respuesta_defensa`.", "info")
    elif respuesta_ataque == 'Dragon' and respuesta_defensa == 'Normal':
        hyperlink("¡Correcto! Has identificado correctamente las fortalezas y debilidades. Avanza a la siguiente sala.", "4.html", "success")
    else:
        text("Revisa bien los datos... ¿Estás seguro de haber calculado los promedios correctamente?", "warning")

def salon_44(col_x, col_y, respuesta):
    import pandas as pd
    url = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'
    df = pd.read_csv(url)
    
    if col_x is None or col_y is None or respuesta is None:
        text("Debes definir las variables `col_x`, `col_y` y `respuesta`.", "info")
    else:
        df['suma'] = df[col_x] + df[col_y]
        respuesta_correcta = df.loc[df['suma'].idxmax(), 'Name']
        
        if respuesta == respuesta_correcta:
            hyperlink("¡Perfecto! Has dominado la visualización y el análisis de datos. Avanza a la siguiente sala.", "end.html", "success")
        else:
            text("Revisa bien... parece que no sumaste correctamente o elegiste mal el Pokémon.", "warning")


if __name__ == "__main__":
    salon_0("PYTHON-25")
    salon_1(None)
    salon_1(5)
    salon_1("2")
