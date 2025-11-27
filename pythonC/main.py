from crear import crear_archivo
from agregar import agregar_texto
from leer import leer_archivo
#Archivos de texto 

# open(nombre del archivo, modo)
# Modos:
# 'r' - lectura (por defecto)
# 'w' - escritura (crea un nuevo archivo o sobrescribe uno existente)
# 'x' - creación (crea un nuevo archivo, falla si ya existe)
# 'a' - anexar (agrega contenido al final del archivo)


#try:    
 #   with open("archivo.txt", "r", encoding="utf-8") as f:
 #       print(f.read())
#except FileNotFoundError:
#    print("El archivo no existe, no se puede escribir en modo lectura.")       
print("-----")
print(" 1 - Crear archivo")
print(" 2 - Agregar un texto al archivo")
print(" 3 - Leer archivo")

op = input("Seleccione una opción: ")

if op == "1":
    crear_archivo("archivo.txt")
elif op == "2":
    agregar_texto()

elif op == "3":
    leer_archivo("archivo.txt")
else:
    print("La opción no es válida")

