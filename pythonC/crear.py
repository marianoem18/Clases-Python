nombre_archivo="archivo.txt"
def crear_archivo(nombre_archivo):
    try:
        """Crea un archivo con el nombre especificado."""
        with open(nombre_archivo, 'x') as f:
            f.write("")  # Crea un archivo vacío
        print(f"Archivo '{nombre_archivo}' creado exitosamente.")
    except FileExistsError:
        print(f"El archivo '{nombre_archivo}' ya existe.")