# Programación orientada a objetos
 #La Poo es un paradigma de programación que utiliza "objetos" para representar datos y métodos.
# Modelar el software como si fuese una colección de objetos que interactúan entre sí.

# Clase: Es una plantilla o molde para crear objetos. Define atributos (propiedades) y métodos (funciones) que los objetos de esa clase tendrán.

"""class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo: Propiedad del objeto
        self.edad = edad      # Atributo: Propiedad del objeto

    def saludar(self):
        print (f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")  # Método: Función del objeto



persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

persona1.saludar()
persona2.saludar()"""


""" Abstracción: 
    Esconder los detalles complejos y mostrar solo la funcionalidad esencial al usuario.
    
    Encapsulamiento :Proteger los datos internos de un objeto, para que no se modifiquen directamente desde fuera.

    herencia: 
    Permite crear una nueva clase basada en una clase existente, heredando sus atributos y métodos
    
    polimorfismo: 
    Permite que diferentes clases puedan ser tratadas como instancias de una misma clase base,
"""

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace GUAU!")   

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace MIAU!")           

