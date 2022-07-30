from datetime import datetime
from datetime import timedelta
import sqlite3

#sumarle 6 años a todas las fechas de la columna expire_date de la tabla tarjeta en la base de datos itbank.db
CADUCIDAD_TARJETA = 6
PATH_DB = '/Users/mateo/OneDrive/Desktop/ITBANK/sql/itbank.db'

connection = sqlite3.connect(PATH_DB)
cursor = connection.cursor()
cursor.execute("SELECT * FROM tarjeta ORDER BY card_id")
tarjetas = cursor.fetchall()
for i, tarjeta in enumerate(tarjetas):
    fecha_cadena = tarjeta[4]
    fecha_datetime = datetime.strptime(fecha_cadena, "%Y-%m-%d")
    fecha_futuro = fecha_datetime + timedelta(days=365*6)
    fecha_formateada = fecha_futuro.strftime("%Y-%m-%d")
    print(fecha_formateada)
    y, m, d = fecha_cadena.split("-")
    fecha_nueva = "-".join([str(int(y) + CADUCIDAD_TARJETA), m, d])
    cursor.execute(f"UPDATE tarjeta SET expire_date = '{fecha_nueva}' WHERE card_id = {i + 1}")
connection.commit()
connection.close()

