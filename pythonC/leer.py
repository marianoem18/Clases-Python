def leer_archivo(nombre_archivo):
    nombre_archivo = "archivo.txt"
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            print(f.read())
            
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe. Por favor, cree el archivo primero.")