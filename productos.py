import lista as Lista


class Producto(Lista.Lista):

    def __init__(self, codigo=0, nombre="S/N", descripcion="Nula", precio=0):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        super().__init__()
           
    def __str__(self):
        if len(self.listageneral)>0:
            return f"La lista contiene: {len(self.listageneral)} productos"
        else:
            return f"Codigo: {self.codigo} Nombre: {self.nombre} Descripcion: {self.descripcion} Precio: {self.precio}"

    def cargarDatos(self,lista,nombre="productos"):
        data = self.cargarJSON(lista,nombre)
        return data

    def leerDatos(self,archivo):
        return self.leerJSON(archivo+".json")

    def getDict(self):
        arreglo = []
        if (len(self.listageneral)>0):
            for p in self.listageneral:
                arreglo.append(p.getDict())
            return arreglo
        else:
            return {"Codigo": self.codigo, "Nombre": self.nombre, "Descripcion": self.descripcion, "Precio": self.precio}

    def getObjfromList(self,archivo):
        data = self.leerDatos(archivo)
        for p in data:
            self.listageneral.append(Producto(p["Codigo"],p["Nombre"],p["Descripcion"],p["Precio"]))
        return self.listageneral
        



if __name__ == "__main__":
    producto1 = Producto(1,"Coca Cola","Bebida gaseosa",12.50)
    producto2 = Producto(2,"Pepsi","Bebida gaseosa",12.50)
    producto3 = Producto(3,"Fanta","Bebida gaseosa",12.50)
    producto4 = Producto(4,"Cerveza","Bebida alcoholica",12.50)

    lista = Producto()
    lista.getObjfromList()
    lista.agregarElemento(producto1)
    lista.agregarElemento(producto2)
    lista.agregarElemento(producto3)
    lista.agregarElemento(producto4)
    #lista.cargarDatos(lista.getDict())
   
    print(lista)
    print(len(lista.listageneral))
    
    

    






    
    

    

    
    
    
     
    
    
    


    

   
    
    





"""class Menu:
    def __init__(self):
        self.productos = []
        x = 1
        while x == 1:
            print("1. Agregar Producto")
            print("2. Mostrar Productos")
            print("3. Actualizar Producto")
            print("4. Eliminar Producto")
            print("5. Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                codigo = int(input("Ingrese codigo: "))
                nombre = input("Ingrese nombre: ")
                descripcion = input("Ingrese descripcion: ")
                precio = float(input("Ingrese precio: "))
                producto = Productos(codigo, nombre, descripcion, precio)
                self.productos.append(producto)
                print("Producto agregado!!")
            elif opcion == 2:
                print("Lista de productos: ")
                for producto in self.productos:
                    print(producto)
            elif opcion == 3:
                codigo = int(input("Ingrese codigo: "))
                for producto in self.productos:
                    if producto.codigo == codigo:
                        y=1
                        while y == 1: 
                            print("1. Nombre")
                            print("2. Descripcion")
                            print("3. Precio")
                            print("4. Salir")
                            opcion = int(input("¿Que desea actualizar? "))
                            if opcion == 1:
                                nombre = input("Ingrese nombre: ")
                                producto.nombre = nombre
                            elif opcion == 2:
                                descripcion = input("Ingrese descripcion: ")
                                producto.descripcion = descripcion
                            elif opcion == 3:
                                precio = float(input("Ingrese precio: "))
                                producto.precio = precio
                            elif opcion ==4 :
                                y = 0
                            else:
                                print("Opcion no valida")
            elif opcion == 4:
                codigo = int(input("Ingrese el codigo del producto: "))
                for producto in self.productos:
                    if producto.codigo == codigo:
                        print("¿Es este el producto que desea eliminar?" + producto)
                        resp = input("Si/No")
                        if resp == "Si":
                            self.productos.remove(producto)
                            print("Producto eliminado!!")
                        elif resp == "No":
                            print("Producto no eliminado!!")
                    else:
                        print("Producto no encontrado")
            elif opcion == 5:
                x = 0
            else:
                print("Opcion no valida")

Menu()    
"""
