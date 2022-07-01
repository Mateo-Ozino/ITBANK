"""
    Módulo con funciones utilizable para el filtrado de cheques.
"""

import time
import datetime
import csv

HEADER = ["NroCheque", "CodigoBanco", "CodigoScurusal", "NumeroCuentaOrigen", "NumeroCuentaDestino", "Valor", "FechaOrigen", "FechaPago", "DNI", "Tipo", "Estado"]
SALIDA_VALIDA = {"csv", "pantalla"}
ESTADO_VALIDO = {"aprobado", "pendiente", "rechazado"}
TIPO_VALIDO = {"emitido", "depositado"}

def to_timestamp(fecha):
    """
    Recibe una fecha en formato dd-mm-yyyy.
    Devuelve la misma fecha en formato timestamp.
    """
    return time.mktime(datetime.datetime.strptime(fecha, "%d-%m-%Y").timetuple())

def filtrado(cheque, dni, tipo, estado, rango_fecha):
    """
    Recibe un cheque y las opciones de filtrado.
    Devuelve True si el cheque las cumple, False en caso contrario.
    """
    if cheque["DNI"] != dni: return False
    if cheque["Tipo"] != tipo: return False
    if estado and cheque["Estado"] != estado: return False
    if rango_fecha and (float(cheque["FechaOrigen"]) < rango_fecha[0] or float(cheque["FechaPago"]) > rango_fecha[1]): return False
    return True

def filtro(path, dni, tipo, estado, rango_fecha):
    """
    Recibe un path a un archivo de cheques tipo csv, y la opciones de filtrado.
    Devuelve una lista filtrada de los cheques que cumplen.
    """
    try:
        archivo = open(path)
    except: 
        print("Archivo no encontrado.")
        return None
    cheques_filtrados = []
    with archivo:
        cheques = csv.DictReader(archivo)
        for cheque in cheques:
            if filtrado(cheque, dni, tipo, estado, rango_fecha): cheques_filtrados.append(cheque)
    if not len(cheques_filtrados): print("No se han encontrado cheques que cumplan con los parametros ingresados.")
    return cheques_filtrados
            
def crear_csv(cheques):
    """
    Recibe una lista de cheques y crea un archivo .csv para almacenarlos.
    """
    if not cheques: return
    fecha = int(datetime.datetime.timestamp(datetime.datetime.now()))
    path = cheques[0]["DNI"] + str(fecha) + ".csv"
    with open(path, "w", newline='') as f:
        cheques_writer = csv.DictWriter(f, fieldnames=HEADER)
        cheques_writer.writeheader()
        cheques_writer.writerows(cheques)

def separar_argumentos(args):
    """
    Recibe un arreglo con los argumentos pasados por línea de comando.
    Devuelve los argumentos por separado, None en el caso de que ese argumento no haya sido ingresado.
    """
    path, dni, salida, tipo = args[:4]
    estado, fecha = None, None
    if len(args) > 4: 
        argumento = args[4]
        if argumento.lower in ESTADO_VALIDO: estado = argumento
        else: fecha = argumento
    elif len(args) > 5: 
        estado = args[4]
        fecha = args[5]
    return path, dni, salida, tipo, estado, fecha