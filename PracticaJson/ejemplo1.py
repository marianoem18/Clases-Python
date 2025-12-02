import json
class Producto:
    def __init__(self, name, price, quantity, brand, category, entry_date):
        self.name = name
        self.price = price
        self.quantity= quantity
        self.brand = brand
        self.category = category
        self.entry_date = entry_date

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "brand": self.brand,
            "category": self.category,
            "entry_date": self.entry_date
        }    
    @staticmethod
    def from_dict(obj):
        return Producto(
            obj["name"],
            obj["price"],
            obj["quantity"],
            obj["brand"],
            obj["category"],
            obj["entry_date"])
    


class GestorProductos:
    def __init__(self):
        self.productos = []
    def cargar(self, archivo="products.json"):
        try:
             with open(archivo, mode='r') as file:
                data=json.load(file)
        except FileNotFoundError:
            print("El archivo no existe. Se creará uno nuevo al guardar.")
            return  
         
        self.productos= [Producto.from_dict(item) for item in data] 
        print("Productos cargados exitosamente.")   

    def guardar(self, archivo="products.json"):
        data = [p.to_dict() for p in self.productos]

        with open(archivo, mode='w',encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)
        print("Productos guardados exitosamente.")


    def listar(self):
        if not self.productos:
            print("No hay productos para mostrar.")
            return
        print("Lista de Productos:")
        for p in self.productos:
            print(f"Nombre: {p.name}, Precio: {p.price}, Cantidad: {p.quantity}, Marca: {p.brand}, Categoría: {p.category}, Fecha de Ingreso: {p.entry_date}")

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado exitosamente.")  

    def main():
        gestor = GestorProductos()
        gestor.cargar()

        while True:
            print("\nMenú de Gestión de Productos")
            print("1. Listar Productos")
            print("2. Agregar Producto")
            print("3. Guardar y Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                gestor.listar()
            elif opcion == '2':
                name = input("Nombre del producto: ")
                price = float(input("Precio del producto: "))
                quantity = int(input("Cantidad del producto: "))
                brand = input("Marca del producto: ")
                category = input("Categoría del producto: ")
                entry_date = input("Fecha de ingreso (YYYY-MM-DD): ")

                nuevo = Producto(name, price, quantity, brand, category, entry_date)
                gestor.agregar_producto(nuevo)
                print("Producto agregado exitosamente")
               
            elif opcion == '3':
                gestor.guardar()
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")    

if __name__ == "__main__":
    GestorProductos.main()



