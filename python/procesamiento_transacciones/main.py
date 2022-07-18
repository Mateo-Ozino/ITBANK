import json
import sys
from datetime import datetime 

import clientes
from generador_razones import *


def cargar_datos(path):
    """
    Recibe una dirección a un archivo con las transacciones de un cliente y su información.
    Devuelve un objeto del tipo Cliente con la información y una lista con todas las transacciones.
    """
    with open(path) as f:
        datos = json.load(f)
        if datos['tipo'] == 'CLASSIC':
            cliente = clientes.Classic(
                datos['nombre'], datos['apellido'], datos['numero'], datos['dni'], datos['direccion'])
        elif datos['tipo'] == 'GOLD':
            cliente = clientes.Gold(
                datos['nombre'], datos['apellido'], datos['numero'], datos['dni'], datos['direccion'])
        elif datos['tipo'] == 'BLACK':
            cliente = clientes.Black(
                datos['nombre'], datos['apellido'], datos['numero'], datos['dni'], datos['direccion'])

    return cliente, datos['transacciones']

def generar_informe(cliente, transacciones):
    """
    Recibe un cliente y una lista de sus transacciones con razones generadas.
    Se encarga de crear un archivo .html con un informe de las transacciones y, en caso de que hayan sido rechazadas, el porqué del rechazo.
    """
    datos = str(cliente).split('\n')
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Transacciones</title>
    <style>
        li {
            list-style: none;
            font-size: 1.2em;
        }
        p {
            font-size: 1.2em;
            padding-left: 1em;
        }
    </style>
</head>
<body>
    <main>
        <h1>Informe de transacciones</h1>"""
    for dato in datos:
        html += f"""
        <li>{dato}</li>"""
        
    for transaccion in transacciones:
        html += f"""
        <div>
            <h3>{transaccion['fecha']} {transaccion['tipo']}: {'Aceptada' if transaccion['estado'] == 'ACEPTADA' else 'Rechazada.'}</h3>
            {'<p>Razón: ' + transaccion['razon'].get_mensaje() + '</p>' if transaccion['estado'] == 'RECHAZADA' else ''}
        </div>
        """

    html +=  """
    </main>
</body>
</html>
    """       
    return html.lstrip('\n')  

    


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print('Cantidad de argumentos incorrecta')
        return

    cliente, transacciones = cargar_datos(args[0])
    for transaccion in transacciones:
        transaccion["razon"] = crear_razon(cliente, transaccion)

    html = generar_informe(cliente, transacciones)

    dt = datetime.now()
    nombre = str(cliente.get_numero()) + '_' + str(int(datetime.timestamp(dt))) + ".html" 
    with open(nombre, 'w', encoding="utf-8") as f:
        f.write(html)

main()