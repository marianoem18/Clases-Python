def agregar_texto():
    nombre_archivo = "archivo.txt"
    try:
        with open(nombre_archivo, "a", encoding="utf-8") as f:

            f.write("Texto agregado al archivo.")
        print(f"Texto agregado al archivo '{nombre_archivo}' exitosamente.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe. Por favor, cree el archivo primero.")