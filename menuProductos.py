"""MENU PRODUCTOS"""

from productos import Producto
from time import sleep
import os
from mongo import MongoConnection

class InterfazProducto:

    def __init__(self):
        self.listaprod = Producto()
        self.listaprod.getObjfromList("productos")
        self.mongo = MongoConnection()

    def limpiarPantalla(self):
        sleep(3)
        os.system("cls")

    def agregarProducto(self):
        print("Ingrese los datos del producto: ")
        codigo = input("Ingrese el codigo: ")
        nombre = input("Ingrese el nombre: ")
        descripcion = input("Ingrese una descripcion: ")
        precio = float(input("Ingrese el precio: "))
        producto = Producto(codigo, nombre, descripcion, precio)
        self.listaprod.agregarElemento(producto)
        self.mongo.tryToSave("Tienda","Productos",self.listaprod.getDict(),producto)
        self.listaprod.cargarDatos(self.listaprod.getDict())
        print("Producto creado!!")
        #print(producto)
        #self.limpiarPantalla()
        
    def mostrarLista(self):
        lista = self.listaprod.leerDatos("productos")
        print("Lista de productos:")
        print("Codigo \tNombre \t\tDescripcion \tPrecio")
        for producto in lista:
            print(producto["Codigo"], "\t"+producto["Nombre"],"\t" +producto["Descripcion"], "\t"+str(producto["Precio"]))
        self.limpiarPantalla()
        
    def eliminarProducto(self):
        codigo = input("Ingrese el codigo del producto a eliminar: ")
        for producto in self.listaprod.mostrarElementos():
            if producto.codigo == codigo:
                self.listaprod.eliminarElemento(producto)
                print("Producto eliminado!!")
        self.listaprod.cargarDatos(self.listaprod.getDict())
        self.limpiarPantalla()
        
    def actualizarProducto(self):
        codigo = input("Ingrese el codigo del producto a modificar: ")
        for producto in self.listaprod.mostrarElementos():
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
                        break
                    else:
                        print("Opcion no valida")
        self.listaprod.cargarDatos(self.listaprod.getDict())
        self.limpiarPantalla()

    def Inicio(self):
        x=1
        while x==1:
            print("Menu de productos")
            print("Seleccione la acción que desea realizar")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Modificar producto")
            print("4. Listar productos")
            print("5. Salir")        
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                self.agregarProducto()
            elif opcion == 2:
                self.eliminarProducto()
            elif opcion == 3:
                self.actualizarProducto()
            elif opcion == 4:
                self.mostrarLista()
            elif opcion == 5:
                print("Hasta luego")
                x = 0
                break
        



if __name__ == "__main__": 
    x = 1
    Menu = InterfazProducto()
    Menu.listaprod.leerDatos()
    while x == 1:
        opcion = Menu.Inicio()
        if opcion == 1:
            Menu.agregarProducto()
        elif opcion == 2:
            Menu.eliminarProducto()
        elif opcion == 3:
            Menu.actualizarProducto()
        elif opcion == 4:
            Menu.mostrarLista()
        elif opcion == 5:
            print("Hasta luego")
            x = 0
    