# Trabajo Práctico Final – Python

## Objetivo
Desarrollar una aplicación web sencilla utilizando **Python**, **pandas** y **Streamlit** que permita analizar y visualizar un catálogo de productos a partir de un archivo CSV.

El objetivo del trabajo es integrar los conceptos vistos durante el curso:
- Lectura de archivos
- Manipulación de datos con pandas
- Lógica básica
- Visualización de información con Streamlit

---

## Datos
Se provee un archivo llamado `catalogo.csv` que contiene información de productos, con las siguientes columnas:

- `codigo`: identificador del producto  
- `nombre`: nombre del producto  
- `precio`: precio unitario  
- `tipo`: categoría del producto  
- `cantidad`: stock disponible  

---

## Consigna
Crear una aplicación en **Streamlit** que permita:

### 1. Cargar y mostrar los datos
- Leer el archivo `catalogo.csv` utilizando pandas.
- Mostrar el catálogo completo en una tabla.

### 2. Filtrar productos
- Permitir filtrar los productos por:
  - Tipo de producto
  - Rango de precios

### 3. Análisis del catálogo
La aplicación debe mostrar:
- El **producto más caro**
- El **producto más barato**
- El **precio promedio** de los productos
- La **cantidad total de stock** disponible

### 4. Visualización
- Mostrar los resultados de forma clara utilizando los componentes de Streamlit (`dataframe`, `metric`, etc.).

---

## Requisitos
- Usar Python
- Usar pandas para el manejo de datos
- Usar Streamlit para la interfaz
- El código debe estar ordenado y comentado
- La aplicación debe poder ejecutarse correctamente

---

## Entrega
- Archivo `.py` con el código de la aplicación
- ---------------------------------------------------------------------------------------------------
# Continuación Trabajo Práctico – CRUD de Productos con SQLite y Streamlit

## Contexto
En la clase anterior se realizó la migración de los datos desde un archivo CSV a una base de datos SQLite (`productos.db`).  
A partir de ahora, la aplicación **ya no trabaja con archivos**, sino directamente con una base de datos.

En este trabajo práctico, se deberá ampliar la aplicación para permitir **gestionar los productos** mediante operaciones CRUD.

---

## Objetivo
Modificar la aplicación desarrollada en Streamlit para que permita **crear, leer, actualizar y eliminar productos** almacenados en una base de datos SQLite.

El objetivo principal es comprender cómo una aplicación interactúa con una base de datos en tiempo real.

---

## ¿Qué es un CRUD?
CRUD es un conjunto de operaciones básicas sobre una base de datos:

- **Create** → Crear registros
- **Read** → Leer registros
- **Update** → Actualizar registros
- **Delete** → Eliminar registros

Estas operaciones son la base de cualquier sistema real.

---

## Base de datos
Se trabajará con la base de datos `productos.db`, que contiene la tabla `productos` con los siguientes campos:

- `id` (clave primaria)
- `codigo`
- `nombre`
- `precio`
- `tipo`
- `cantidad`

---

## Consignas

### 1. Lectura de datos (READ)
La aplicación debe:

- Conectarse a la base de datos SQLite.
- Obtener todos los productos desde la tabla `productos`.
- Convertir los datos en un DataFrame utilizando pandas.
- Mostrar el listado de productos en la aplicación.

👉 Esta operación reemplaza completamente la lectura del archivo CSV.

---

### 2. Alta de productos (CREATE)
La aplicación debe permitir:

- Ingresar los datos de un nuevo producto desde la interfaz de Streamlit.
- Validar que los campos no estén vacíos.
- Insertar el nuevo producto en la base de datos.
- Actualizar la vista para mostrar el nuevo producto agregado.

📌 Esta operación debe utilizar una consulta SQL de tipo `INSERT`.

---

### 3. Modificación de productos (UPDATE)
La aplicación debe permitir:

- Seleccionar un producto existente (por ejemplo, usando su `id` o nombre).
- Mostrar los datos actuales del producto.
- Modificar uno o más campos.
- Guardar los cambios en la base de datos.
- Refrescar la información mostrada.

📌 Esta operación debe utilizar una consulta SQL de tipo `UPDATE`.

---

### 4. Eliminación de productos (DELETE)
La aplicación debe permitir:

- Seleccionar un producto existente.
- Confirmar la eliminación del producto.
- Eliminar el producto de la base de datos.
- Actualizar la lista de productos mostrada.

📌 Esta operación debe utilizar una consulta SQL de tipo `DELETE`.

---

## Uso de Streamlit
Para la interfaz, se recomienda utilizar:

- Formularios para carga y edición de productos.
- Selectores para elegir productos.
- Botones para confirmar acciones.
- Mensajes de éxito o error para informar al usuario.

La aplicación debe ser clara y fácil de usar.

---

## Uso de SQLite
Para la base de datos, se deberá:

- Utilizar la librería `sqlite3`.
- Crear funciones separadas para cada operación CRUD.
- Abrir y cerrar correctamente la conexión a la base de datos.
- Confirmar los cambios realizados (commit).

---

## Requisitos
- Usar Python
- Usar Streamlit
- Usar SQLite
- Usar pandas para mostrar datos
- Mantener el código ordenado y comentado
- No utilizar más el archivo CSV como fuente de datos

---

## Concepto clave del trabajo
> La aplicación ahora puede modificar los datos en tiempo real.

---

## Entrega
- Archivo `productos.db`
- Código actualizado de la aplicación en Streamlit
- La aplicación debe permitir crear, leer, modificar y eliminar productos correctamente

