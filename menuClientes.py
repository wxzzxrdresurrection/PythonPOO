"""MENU CLIENTES"""
from clientes import Cliente
import os
from time import sleep
from mongo import MongoConnection

class InterfazCliente:

    def __init__(self):
        self.listaclientes = Cliente()
        self.listaclientes.getObjfromList("lista de clientes")
        self.mongo = MongoConnection()

    def limpiarPantalla(self):
        sleep(3)
        os.system("cls")

    def agregarCliente(self):
        print("Ingrese los datos del ciente:")
        rfc = input("RFC:")
        nombre = input("Nombre:")
        telefono = input("Telefono:")
        ncliente = Cliente(rfc,nombre,telefono)
        self.listaclientes.agregarElemento(ncliente)
        self.mongo.tryToSave("Tienda","Clientes",self.listaclientes.getDict(),ncliente)
        self.listaclientes.cargarDatos(self.listaclientes.getDict())
        print("Cliente creado y agregado a la lista")
        print(ncliente)
        self.limpiarPantalla()

    def eliminarCliente(self):
        rfc = input("Ingrese el RFC del cliente a eliminar: ")
        for cliente in self.listaclientes.mostrarElementos():
            if cliente.rfc == rfc:
                self.listaclientes.eliminarElemento(cliente)
        self.listaclientes.cargarDatos(self.listaclientes.getDict())
        self.limpiarPantalla()

    def mostrarClientes(self):
        lista = self.listaclientes.leerDatos("lista de clientes")
        print("Lista de clientes: ")
        if len(lista) == 0:
            print("No hay clientes")
        else:
            print(self.listaclientes)
            for cliente in lista:
                print(cliente)
        self.limpiarPantalla()

    def actualizarCliente(self):
        rfc = input("Ingrese el RFC del cliente a modificar: ")
        for cliente in self.listaclientes.mostrarElementos():
            if cliente.rfc == rfc:
                y=1
                while y == 1:
                    print("1. Nombre")
                    print("2. Telefono")
                    print("3. Salir")
                    opcion = int(input("¿Que desea actualizar? "))
                    if opcion == 1:
                        nombre = input("Ingrese el nuevo nombre: ")
                        cliente.nombre = nombre
                    elif opcion == 2:
                        telefono = input("Ingrese el nuevo telefono: ")
                        cliente.telefono = telefono
                    elif opcion == 3:
                        y=0
                    else:
                        print("Opcion no valida")
        self.listaclientes.cargarDatos(self.listaclientes.getDict())
        self.limpiarPantalla()

    def menuPrincipal(self):
        x=1
        while x == 1:
            print("1. Agregar cliente")
            print("2. Eliminar cliente")
            print("3. Mostrar clientes")
            print("4. Actualizar cliente")
            print("5. Salir")
            opcion = int(input("¿Que desea hacer? "))
            if opcion ==1:
                self.agregarCliente()
            elif opcion ==2:
                self.eliminarCliente()  
            elif opcion ==3:
                self.mostrarClientes()
            elif opcion ==4:
                self.actualizarCliente()
            elif opcion ==5:
                x=0
            
    

if __name__ == "__main__":
    x = 1
    menu = InterfazCliente()
    menu.listaclientes.leerDatos()
    while x == 1:
        opcion = menu.menuPrincipal()
        if opcion == 1:
            menu.agregarCliente()
        if opcion == 2:
            menu.eliminarCliente()
        if opcion == 3:
            menu.mostrarClientes()
        if opcion == 4:
            menu.actualizarCliente()
        if opcion == 5:
            print("Saliendo menu clientes...")
            x = 0
            menu.limpiarPantalla()



        
