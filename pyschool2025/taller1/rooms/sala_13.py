from helpers import text, hyperlink

def revisar(respuesta):

    diccionario = {'ps01': ['lab_ps01', 'quimicos_ps01', 'sustancias_ps01'], 'ec00': ['rendimiento_ec00', 'paneles_ec00', 'reporte_ec00'], 'tc12': ['pruebas_tc12', 'bateria_tc12', 'reparaciones_salas_tc12']}

    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == diccionario:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_14.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def ordenar_archivos(archivos):

    diccionario = {}

    for archivo in archivos:

        sufijo = archivo[-4:]
        if sufijo not in diccionario:
            diccionario[sufijo] = [archivo]

        else:
            diccionario[sufijo].append(archivo)

    return diccionario

if __name__ == "__main__":
    nombres_archivos = ["lab_ps01", "rendimiento_ec00", "pruebas_tc12", "quimicos_ps01", "bateria_tc12", "paneles_ec00",
                        "reporte_ec00", "reparaciones_salas_tc12", "sustancias_ps01"]

    revisar(None)
    revisar(ordenar_archivos(nombres_archivos))
    revisar(False)
