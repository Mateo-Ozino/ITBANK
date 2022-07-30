import sqlite3
import random

PATH_DB = "/Users/mateo/OneDrive/Desktop/ITBANK/sql/itbank.db"
TIPOS_CLIENTE = ["CLASSIC", "GOLD", "BLACK"]

def asignacion_cliente_tipos(cantidad):
    conexion = sqlite3.connect(PATH_DB)
    cursor = conexion.cursor()
    for customer_id in range(cantidad):
        cursor.execute(f"UPDATE cliente SET client_type = '{random.choice(TIPOS_CLIENTE)}' WHERE customer_id = {customer_id + 1}")
    conexion.commit()
    conexion.close()

asignacion_cliente_tipos(500)