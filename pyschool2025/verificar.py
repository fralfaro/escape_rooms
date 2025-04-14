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

if __name__ == "__main__":
    salon_0("PySchool2025")
    salon_1(None)
    salon_1(5)
    salon_1("2")
