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
# Trabajo Práctico – Sistema de Login con SQLite y Streamlit

## Contexto
Actualmente, la aplicación permite visualizar un catálogo de productos utilizando una base de datos SQLite.  
En este trabajo práctico se agregará un **sistema de autenticación**, permitiendo que solo los usuarios registrados puedan acceder a la aplicación.

Este tipo de funcionalidad es común en aplicaciones reales y permite controlar el acceso a la información.

---

## Objetivo
Agregar un sistema de **login de usuarios** a la aplicación desarrollada en Streamlit, utilizando una base de datos SQLite para almacenar las credenciales.

---

## Base de datos
Se trabajará con la base de datos existente (`productos.db`) y se deberá agregar una nueva tabla llamada `usuarios`, con los siguientes campos:

- `id` (entero, clave primaria)
- `username` (texto)
- `password` (texto)

---

## Consignas

### 1. Crear la tabla de usuarios
- Crear la tabla `usuarios` en la base de datos.
- Insertar al menos un usuario de prueba.

---

### 2. Pantalla de login
La aplicación debe mostrar inicialmente:
- Un campo para ingresar el nombre de usuario.
- Un campo para ingresar la contraseña.
- Un botón para iniciar sesión.

---

### 3. Validación de credenciales
- Al presionar el botón de login, la aplicación debe:
  - Consultar la base de datos.
  - Verificar si el usuario existe.
  - Comparar la contraseña ingresada con la almacenada.
- Si los datos son correctos, permitir el acceso a la aplicación.
- Si los datos son incorrectos, mostrar un mensaje de error.

---

### 4. Acceso al catálogo
- Solo los usuarios autenticados deben poder ver el catálogo de productos.
- Si el usuario no está autenticado, no debe poder acceder a los datos.

---

## Requisitos
- Usar Python
- Usar Streamlit
- Usar SQLite
- Mantener el código ordenado y comentado

---

## Concepto clave del trabajo
> El acceso a la información debe estar controlado.

---

## Entrega
- Base de datos actualizada (`productos.db`)
- Código de la aplicación con sistema de login funcionandot



