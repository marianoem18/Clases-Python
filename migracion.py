import sqlite3
import pandas as pd

# -----------------------------
# CONEXIÓN A LA BASE DE DATOS
# -----------------------------

conn = sqlite3.connect("productos.db")
cursor = conn.cursor()

# -----------------------------
# CREAR TABLA
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT,
    nombre TEXT,
    precio REAL,
    tipo TEXT,
    cantidad INTEGER
)
""")

# -----------------------------
# VERIFICAR SI YA HAY DATOS
# -----------------------------

cursor.execute("SELECT COUNT(*) FROM productos")
cantidad_registros = cursor.fetchone()[0]

if cantidad_registros == 0:
    # Leer CSV
    df = pd.read_csv("catalogo.csv")

    # Insertar datos en la base
    df.to_sql(
        "productos",
        conn,
        if_exists="append",
        index=False
    )

    print("Migración realizada correctamente.")
else:
    print("La base de datos ya contiene datos. No se realizó la migración.")

# -----------------------------
# CERRAR CONEXIÓN
# -----------------------------

conn.commit()
conn.close()
