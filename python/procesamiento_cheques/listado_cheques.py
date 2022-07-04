"""
    Este programa se encarga de leer y filtrar un archivo de cheques de 
    formato csv según parámetros pasados por línea de comandos.
"""

import sys
from biblioteca_filtrado import *

def main():
    args = sys.argv[1:] 

    if len(args) < 4 or len(args) > 6:
        print("Cantidad de elementos errónea.")
        return

    path, dni, salida, tipo, estado, fecha = separar_argumentos(args)

    son_validos = [
        salida.lower() in SALIDA_VALIDA,
        tipo.lower() in TIPO_VALIDO,
        not estado or estado.lower() in ESTADO_VALIDO,
    ]
    if not all(son_validos): 
        print("Parámetros inválidos.")
        return

    rango_fecha = None
    if fecha:
        try:
            rango_fecha = fecha.split(":")
            rango_fecha[0] = to_timestamp(rango_fecha[0])
            rango_fecha[1] = to_timestamp(rango_fecha[1])
            rango_fecha = tuple(rango_fecha)
        except:
            print("Parámetros inválidos.")
            return

    cheques_filtrados = filtro(path, dni, tipo, estado, rango_fecha)

    if not cheques_filtrados: return

    if salida.lower() == "pantalla":
        for cheque in cheques_filtrados:
            imprimir_cheque(cheque)
    elif salida.lower() == "csv":
        crear_csv(cheques_filtrados)

main()