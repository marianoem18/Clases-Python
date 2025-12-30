# Clase 10: Introducción a Bases de Datos con SQLite en Python

**Bienvenidos a la Clase 10 del curso de Python en la UTN FRT.**

Hoy introduciremos un tema fundamental para cualquier desarrollador: las bases de datos. Usaremos **SQLite**, una base de datos ligera y fácil de usar que viene integrada en Python, sin necesidad de instalaciones extras. Esto nos permitirá almacenar datos de manera persistente, más allá de archivos JSON o APIs temporales.

En clases anteriores manejamos datos en memoria (con Pandas) o desde fuentes externas (APIs). Las bases de datos resuelven el problema de “dónde guardar los datos para que no se pierdan cuando el programa termina”. Explicaremos todo desde cero, asumiendo que nadie sabe nada de bases de datos.

La clase dura 2 horas virtuales: los primeros 90 minutos serán explicación conceptual, código guiado y ejemplos prácticos; los últimos 30 minutos un ejercicio corto. Al final, presentaremos el enunciado del Trabajo Práctico integrador.

No necesitan instalar nada nuevo: SQLite está en Python por defecto.

## 1. Repaso Rápido de Datos en Python

Antes de entrar en bases de datos, recordemos cómo manejamos datos hasta ahora.

**Datos en memoria o archivos temporales:**

- En Pandas, cargamos datos en DataFrames (tablas en memoria):

```python
import pandas as pd
df = pd.read_json('products.json')
print(df.head()) ```

Esto es genial para análisis, pero si el programa termina, los cambios no se guardan automáticamente.
Problema que resuelven las bases de datos:
Imagina una app de tienda: quieres guardar ventas nuevas permanentemente, no perderlas al cerrar el programa. Las bases de datos almacenan datos en disco de forma estructurada y segura.
Si tienen dudas del repaso (e.g., Pandas o APIs), pregunten ahora.
2. Introducción Conceptual a Bases de Datos
Explicaremos todo como si fuera la primera vez que oyen estos términos. Usaremos analogías simples.
¿Qué es una base de datos (DB)?
Una base de datos es un “almacén organizado” de información, como un archivo Excel gigante pero más poderoso y seguro. Permite guardar, buscar, actualizar y eliminar datos de manera eficiente.
A diferencia de un archivo JSON (que es plano y se carga todo en memoria), una DB puede manejar millones de registros sin colapsar tu programa y soporta consultas complejas (e.g., “muéstrame solo productos caros de una marca”).
Tipos de bases de datos (simplificado):

Relacionales (como SQLite): Organizadas en “tablas” (como hojas de Excel). Cada tabla tiene columnas (atributos, e.g., “nombre”, “precio”) y filas (registros, e.g., un producto específico). Usan SQL para interactuar. Son ideales para datos estructurados con relaciones.
No relacionales (e.g., MongoDB): Más flexibles, como documentos JSON. No las veremos hoy.

Nos enfocamos en relacionales porque son las más comunes y fáciles de entender al principio.
Conceptos clave en una DB relacional (con analogías):

Tabla: Una estructura como una tabla de Excel. Ejemplo: Tabla “Productos” con columnas “id”, “nombre”, “precio”, “categoria”.
Fila (o registro): Una entrada individual en la tabla. Ejemplo: Fila 1: id=1, nombre=“Laptop”, precio=999.99, categoria=“Electrónicos”.
Columna (o campo): Un atributo común a todas las filas. Ejemplo: La columna “precio” solo guarda números.
Clave primaria (Primary Key): Un identificador único para cada fila, como un DNI. Evita duplicados. Ejemplo: “id” autoincremental (1,2,3…).
SQL: El lenguaje para “hablar” con la DB. Es como comandos en inglés: “SELECT” para leer, “INSERT” para agregar, etc. No es Python, pero lo usamos dentro de Python.
Conexión: Para acceder a la DB, “conectas” tu programa como si abrieras un archivo.
Cursor: Un “puntero” que ejecuta comandos SQL y trae resultados. Como un mouse en la DB.
Transacciones: Grupos de operaciones que se hacen “todo o nada” para evitar errores (e.g., si fallas al insertar, revierte todo). Usamos “commit” para confirmar cambios.

¿Por qué usar una DB en lugar de JSON o CSV?

Persistencia: Los datos sobreviven al cierre del programa.
Eficiencia: Consultas rápidas en grandes datasets (e.g., buscar por filtro sin cargar todo).
Seguridad: Soporta usuarios, permisos y backups.
Relaciones: Puedes unir tablas (e.g., tabla “Productos” con “Ventas”).

SQLite es perfecta para principiantes: es un archivo simple (.db), no necesita servidor, y es gratis/incluida en Python. En proyectos grandes, usarías MySQL o PostgreSQL, pero el concepto es igual.
3. Instalación y Primer Contacto con SQLite
No hay instalación: SQLite viene con Python. Solo importa el módulo.
Primer ejemplo: Crear y conectar a una DB
Pythonimport sqlite3

# Conectar (o crear si no existe) a la DB 'mi_base.db'
conn = sqlite3.connect('mi_base.db')
print("Conexión exitosa!")

# Siempre cierra al final
conn.close()
Explicación paso a paso:

import sqlite3: Biblioteca estándar de Python para SQLite.
conn = sqlite3.connect('mi_base.db'): Crea/conecta a un archivo .db. Si no existe, lo crea vacío. “conn” es la conexión, como un cable a la DB.
conn.close(): Cierra la conexión para liberar recursos. Siempre hazlo al final, o usa with para auto-cierre.

Ejecútenlo: Verán un archivo 'mi_base.db' en su carpeta.
Crear una tabla con SQL
Pythonconn = sqlite3.connect('mi_base.db')

# Crear un cursor (el "ejecutor" de comandos)
cursor = conn.cursor()

# Comando SQL para crear tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL,
    categoria TEXT
)
''')

# Confirmar cambios
conn.commit()
conn.close()
Explicación detallada:

cursor = conn.cursor(): Crea un cursor para ejecutar SQL.
cursor.execute('SQL aquí'): Ejecuta el comando. El SQL crea una tabla “productos” si no existe (“IF NOT EXISTS” evita errores).
id INTEGER PRIMARY KEY AUTOINCREMENT: Columna ID numérica, única, auto-incrementa (1,2,3…).
nombre TEXT NOT NULL: Columna texto, obligatoria (“NOT NULL”).
precio REAL: Columna para números decimales.
categoria TEXT: Columna texto opcional.

conn.commit(): Guarda los cambios permanentemente (como “save” en un documento). Sin esto, los cambios se pierden.

Esto es como crear una hoja de Excel vacía con columnas definidas.
4. Operaciones Básicas con SQL en SQLite
Ahora, aprendamos los comandos SQL clave: INSERT (agregar), SELECT (leer), UPDATE (actualizar), DELETE (eliminar). Usaremos nuestra tabla “productos”.
INSERT: Agregar datos
Pythonconn = sqlite3.connect('mi_base.db')
cursor = conn.cursor()

# Insertar un registro
cursor.execute('''
INSERT INTO productos (nombre, precio, categoria) 
VALUES ('Laptop', 999.99, 'Electrónicos')
''')

conn.commit()
conn.close()
Explicación:

INSERT INTO tabla (columnas) VALUES (valores): Agrega una fila. Nota: No incluimos “id” porque auto-incrementa.
Ejecuta varias veces para agregar más: Cambia valores para probar.

SELECT: Leer datos
Pythonconn = sqlite3.connect('mi_base.db')
cursor = conn.cursor()

# Seleccionar todo
cursor.execute('SELECT * FROM productos')
resultados = cursor.fetchall()  # Trae todos los registros como lista de tuplas

print(resultados)  # Ej: [(1, 'Laptop', 999.99, 'Electrónicos')]

conn.close()
Explicación:

SELECT * FROM tabla: Trae todas las columnas (*) de la tabla.
cursor.fetchall(): Obtiene todos los resultados como lista de tuplas (cada tupla es una fila).
Variaciones: SELECT nombre, precio FROM productos (solo esas columnas).
Filtros: SELECT * FROM productos WHERE precio > 500 (condiciones con WHERE).
Orden: SELECT * FROM productos ORDER BY precio DESC (descendente).

UPDATE: Actualizar datos
Pythonconn = sqlite3.connect('mi_base.db')
cursor = conn.cursor()

# Actualizar precio de un producto
cursor.execute('''
UPDATE productos 
SET precio = 899.99 
WHERE id = 1
''')

conn.commit()
conn.close()
Explicación:

UPDATE tabla SET columna = valor WHERE condición: Cambia valores específicos. Sin WHERE, actualiza todo (peligroso!).

DELETE: Eliminar datos
Pythonconn = sqlite3.connect('mi_base.db')
cursor = conn.cursor()

# Eliminar un registro
cursor.execute('DELETE FROM productos WHERE id = 1')

conn.commit()
conn.close()
Explicación:

DELETE FROM tabla WHERE condición: Borra filas específicas. Sin WHERE, borra toda la tabla.

Manejo de múltiples operaciones:
Usa executemany para inserts masivos:
Pythondatos = [('Telefono', 499.99, 'Electrónicos'), ('Libro', 19.99, 'Libros')]
cursor.executemany('INSERT INTO productos (nombre, precio, categoria) VALUES (?, ?, ?)', datos)
Los “?” son placeholders para evitar inyecciones SQL (seguridad).
Practiquen: Agreguen 5 productos, lean con filtro, actualicen uno, borren otro.
5. Integración con Pandas
SQLite se integra perfectamente con Pandas para análisis.
Leer de DB a DataFrame:
Pythonimport pandas as pd
import sqlite3

conn = sqlite3.connect('mi_base.db')
df = pd.read_sql('SELECT * FROM productos', conn)
print(df.head())
conn.close()
Explicación:

pd.read_sql('SQL', conn): Ejecuta el SELECT y carga directamente en DataFrame. Ideal para filtros complejos en DB antes de analizar en Pandas.

Escribir de DataFrame a DB:
Pythondf.to_sql('productos_nuevos', conn, if_exists='replace', index=False)

to_sql(tabla, conn, if_exists='replace'): Crea/reemplaza una tabla con los datos del DF. index=False evita agregar el índice de Pandas como columna.

Esto une lo mejor: DB para almacenamiento persistente, Pandas para análisis.
6. Buenas Prácticas y Manejo de Errores

Usa with para auto-cierre:

Pythonwith sqlite3.connect('mi_base.db') as conn:
    cursor = conn.cursor()
    # Operaciones aquí
    conn.commit()  # Commit dentro del with
Cierra automáticamente.

Manejo de errores:

Usa try/except:
Pythontry:
    cursor.execute(sql)
except sqlite3.Error as e:
    print(f"Error en DB: {e}")
Errores comunes: Sintaxis SQL mala, tabla inexistente.

Seguridad: Usa placeholders (?) en lugar de concatenar strings para evitar SQL injection (ataques).
Backups: Copia el .db como archivo normal.
Límites de SQLite: Bueno para apps locales/pequeñas; para web/multi-usuario, migra a PostgreSQL.
Conceptos avanzados (para futuro): Joins (unir tablas), índices (acelerar búsquedas), transacciones (BEGIN TRANSACTION).

7. Ejercicio Práctico
Instrucciones:
Creen un script gestion_productos.py para una “mini-tienda” con SQLite.
Funcionalidades mínimas:

Crea/conecta a 'tienda.db'.
Crea tabla “inventario” con id, producto (text), cantidad (integer), precio (real).
Agrega al menos 3 productos con INSERT.
Lee todo con SELECT y muestra en consola (usa fetchall o Pandas).
Actualiza la cantidad de un producto (e.g., resta 1 por “venta”).
Elimina un producto con stock 0.
Maneja errores con try/except.
