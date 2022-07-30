import sqlite3
import random

PATH_DB = "/Users/mateo/OneDrive/Desktop/ITBANK/sql/itbank.db"

#Agregamos 100 direcciones al azar y sin repetir a las sucursales (1 por sucursal)
def agregar_direcciones_sucursales(cantidad):
    conexion = sqlite3.connect(PATH_DB)
    cursor = conexion.cursor()
    direcciones = [i + 1 for i in range(cantidad)]
    random.shuffle(direcciones)
    for branch_id, direccion_id in enumerate(direcciones):
        cursor.execute(f"UPDATE sucursal SET direccion_id = {direccion_id} WHERE branch_id = {branch_id + 1}")
    conexion.commit()
    conexion.close()

#agregar_direcciones_sucursales(100)

#Agregamos 500 direcciones al azar a los clientes (1 por cliente)
def agregar_direcciones_clientes(cantidad):
    conexion = sqlite3.connect(PATH_DB)
    cursor = conexion.cursor()
    for customer_id in range(cantidad):
        cursor.execute(f"UPDATE cliente SET direccion_id = {random.randint(101, 500)} WHERE customer_id = {customer_id + 1}")
    conexion.commit()
    conexion.close()

#agregar_direcciones_clientes(500)

#Agregamos 500 direcciones al azar a los empleados (1 por empleado)
def agregar_direcciones_empleados(cantidad):
    conexion = sqlite3.connect(PATH_DB)
    cursor = conexion.cursor()
    for employee_id in range(cantidad):
        cursor.execute(f"UPDATE empleado SET direccion_id = {random.randint(101, 500)} WHERE employee_id = {employee_id + 1}")
    conexion.commit()
    conexion.close()

agregar_direcciones_empleados(500)