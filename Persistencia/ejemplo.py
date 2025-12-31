import sqlite3
import pandas as pd  # Para el extra: mostrar con DataFrame

# Nombre de la base de datos
DB_NAME = 'tienda.db'
 # Agregar al menos 3 productos (INSERT)
productos_iniciales = [
            ('Laptop', 5, 999.99),
            ('Mouse', 20, 25.50),
            ('Teclado', 15, 45.00),
            ('Monitor', 8, 250.00),
            ('Auriculares', 30, 80.00)
        ]

try:
    # Conectar (o crear) la base de datos
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        print("Conexión exitosa a la base de datos!")

        # Crear la tabla "inventario" si no existe
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
        ''')
        print("Tabla 'inventario' creada o ya existente.")

       
        cursor.executemany('''
        INSERT OR IGNORE INTO inventario (producto, cantidad, precio) 
        VALUES (?, ?, ?)
        ''', productos_iniciales)
        print("Productos iniciales agregados (si no existían).")

        # Leer y mostrar todo (SELECT)
        print("\n--- Inventario actual ---")
        cursor.execute('SELECT * FROM inventario')
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)  # Ej: (1, 'Laptop', 5, 999.99)

        # Extra: Mostrar con Pandas para mejor visualización
        df = pd.read_sql('SELECT * FROM inventario', conn)
        print("\nInventario con Pandas:")
        print(df)

        # Actualizar cantidad (simular una "venta" - restar 1 a un producto)
        producto_a_vender = 'Laptop'
        cursor.execute('''
        UPDATE inventario 
        SET cantidad = cantidad - 1 
        WHERE producto = ? AND cantidad > 0
        ''', (producto_a_vender,))
        print(f"\nVenta simulada: 1 unidad de {producto_a_vender} vendida.")

        # Eliminar productos con stock 0
        cursor.execute('''
        DELETE FROM inventario 
        WHERE cantidad <= 0
        ''')
        print("Productos con stock 0 eliminados (si había alguno).")

        # Mostrar inventario final
        print("\n--- Inventario final después de cambios ---")
        df_final = pd.read_sql('SELECT * FROM inventario', conn)
        print(df_final)

except sqlite3.Error as e:
    print(f"Error en la base de datos: {e}")
except Exception as e:
    print(f"Error general: {e}")

print("\n¡Operaciones completadas!")