import sqlite3
import random

PATH_DB = "/Users/mateo/OneDrive/Desktop/ITBANK/sql/itbank.db"
TIPOS_CUENTA = ["Caja de ahorro en pesos", "Caja de ahorro en dolares", "Cuenta corriente"]

def asignacion_cuenta_tipos(cantidad):
    conexion = sqlite3.connect(PATH_DB)
    cursor = conexion.cursor()
    for account_id in range(cantidad):
        cursor.execute(f"UPDATE cuenta SET account_type = '{random.choice(TIPOS_CUENTA)}' WHERE account_id = {account_id + 1}")
    conexion.commit()
    conexion.close()

asignacion_cuenta_tipos(500)