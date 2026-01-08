import sqlite3

# ---------------------------
# CONEXIÓN A LA BASE DE DATOS
# ---------------------------

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

# ---------------------------
# CREAR TABLA USUARIOS
# ---------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

# ---------------------------
# INSERTAR USUARIO DE PRUEBA
# ---------------------------

cursor.execute("""
INSERT OR IGNORE INTO usuarios (username, password)
VALUES (?, ?)
""", ("admin", "1234"))

# ---------------------------
# GUARDAR Y CERRAR
# ---------------------------

conexion.commit()
conexion.close()

print("Tabla usuarios creada correctamente.")
