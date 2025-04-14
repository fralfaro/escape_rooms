# types: warning, danger, success, info, primary
########################################################
# UTILIDADES
########################################################

def text(text="", type="info"):
    text_str = f'<div class="btn btn-{type}" w-100 h-100>{text}</div>'
    print(text_str)


def hyperlink(text, url, type="info"):
    text_str = f'<a href="{url}" class="btn btn-{type} w-100 h-100">{text}</a>'
    print(text_str)


########################################################
# SALONES
########################################################

def salon_0(answer):
    if answer == "PySchool2025":
        hyperlink("¡Correcto! Avanza a la siguiente página", "1.html", "success")
    else:
        incorrect_answer = f"""Estás probando nuevas respuestas, muy bien.  
        Recuerda que la respuesta es PySchool2025"""
        text(incorrect_answer, "warning")


def salon_1(answer):
    if answer == "Hola Mundo":
        hyperlink("¡Correcto! Avanza a la siguiente página", "2.html", "success")
    elif answer == None:
        text("Indica la solución asignando algún valor a la variable `respuesta`.", "info")
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")


def salon_2(answer):
    #\frac{1.23 + 2.34}{1 + 43/2} + 3 \times 2^{1.5}
    true_answer = (1.23 + 2.34) / (1 + 43/2) + 3 * 2**1.5
    epsilon = 0.000001
    if type(answer) in [float, int] and abs(answer - true_answer) < epsilon:
        hyperlink("¡Correcto! Avanza a la siguiente página", "3.html", "success")
    elif answer == None:
        text("Indica la solución asignando algún valor a la variable `respuesta`.", "info")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def salon_3(edad, color_llave):
    if edad is None or color_llave is None:
        text("Debes asignar valores a las variables `edad` y `color_llave`.", "info")
    elif edad >= 18 and color_llave == "dorado":
        hyperlink("¡Correcto! Avanza a la siguiente sala", "4.html", "success")
    else:
        text("La puerta sigue cerrada... Revisa las condiciones.", "warning")

def salon_4(inicio, fin, multiplo):
    if inicio is None or fin is None or multiplo is None:
        text("Debes asignar valores a las variables `inicio`, `fin` y `multiplo`.", "info")
    elif inicio == 1 and fin == 20 and multiplo == 2:
        hyperlink("¡Correcto! Avanza a la siguiente sala", "5.html", "success")
    else:
        text("La puerta sigue cerrada... Revisa las condiciones.", "warning")

def salon_5(min_length, letra):
    if min_length is None or letra is None:
        text("Debes asignar valores a las variables `min_length` y `letra`.", "info")
    elif min_length == 5 and letra == "a":
        hyperlink("¡Correcto! Avanza a la siguiente sala", "6.html", "success")
    else:
        text("La puerta sigue cerrada... Revisa las condiciones.", "warning")

def salon_6(senal_3, senal_5, senal_15, senal_7):
    if senal_3 is None or senal_5 is None or senal_15 is None or senal_7 is None:
        text("Debes asignar valores a las variables `senal_3`, `senal_5`, `senal_15` y `senal_7`.", "info")
    elif senal_3 == "Py" and senal_5 == "School" and senal_15 == "PySchool" and senal_7 == "Sin señal":
        hyperlink("¡Excelente! Has activado la máquina correctamente y la puerta se abre.", "end.html", "success")
    else:
        text("La puerta sigue cerrada... Revisa las instrucciones y verifica las respuestas esperadas.", "warning")


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
    elif respuesta == 18:
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


if __name__ == "__main__":
    salon_0("PySchool2025")
    salon_1(None)
    salon_1(5)
    salon_1("2")
