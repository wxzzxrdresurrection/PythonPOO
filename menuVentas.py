from ventas import Venta
from time import sleep
from clientes import Cliente
from productos import Producto
from menuProductos import InterfazProducto
from menuClientes import InterfazCliente
import os
import pymongo
from mongo import MongoConnection

class InterfazVenta:

    def __init__(self):
        self.listaventas = Venta()
        self.listaventas.getObjfromList("ventas2")
        self.listaclientes = Cliente()
        self.listaclientes.getObjfromList("lista de clientes")
        self.listaprod = Producto()
        self.listaprod.getObjfromList("productos")
        self.ventasSinConexion =Venta()
        self.mongo = MongoConnection()

    def limiarPantalla(self):
        sleep(3)
        os.system("cls")

    def menuPrincipal(self):
        x=1
        while x == 1:
            print("Menu de ventas")
            print("1.- Nueva venta")
            print("2.- Mostrar ventas")
            print("3.- Eliminar venta")
            print("4.- Actualizar venta")
            print("5.- Mostrar clientes")
            print("6.- Mostrar productos")
            print("7.- Salir")
            opcion = int(input("Ingrese una opcion:"))
            if opcion == 1:
                self.agregarVenta()
            elif opcion == 2:
                self.mostrarVentas()
            elif opcion == 3:
                self.eliminarVenta()
            elif opcion == 4:
                self.actualizarVenta()
            elif opcion == 5:
                self.getClientes()
            elif opcion == 6:
                self.getProductos()
            elif opcion == 7:
                print("Cerrando...")
                x = 0
                self.limiarPantalla()

    def limpiarPantalla(self):
        sleep(3)
        os.system("cls")

    def mostrarVentas(self):
        listaventas = self.listaventas.leerDatos("ventas2")
        print("Lista de ventas:")
        print("Folio \t Cliente \t Productos \t Fecha \t\t Total ")
        for venta in listaventas:
            print(venta["Folio"], "\t", venta["Cliente"]["RFC"], "\t", venta["Detalle productos"][0]["Nombre"], "\t", venta["Fecha"], "\t", venta["Total"])
        self.limpiarPantalla()

    def agregarVenta(self):
        nventa = Venta()
        rfc = input("Ingrese el RFC del cliente: ")
        for cliente in self.listaclientes.mostrarElementos():
            if cliente.rfc == rfc:
                print("Cliente encontrado")
                print(cliente)
                nventa.cliente = cliente
                break
        listaprod = self.listaprod.mostrarElementos()
        print("Lista de productos:")
        for producto in listaprod:
            print(producto)
        cant = int(input("Ingrese la cantidad de productos a comprar: "))
        listaprod2 = Producto()
        for i in range(cant):
            codigo = input("Ingrese el codigo del producto: ")
            for producto in listaprod:
                if producto.codigo == codigo:
                    print("Producto encontrado")
                    print(producto)
                    listaprod2.agregarElemento(producto)
        nventa.detalles_producto = listaprod2
        print("Productos agregados a la venta")
        print("Ingrese los datos de la venta:")
        nventa.folio = input("Folio:")
        nventa.fecha = input("Fecha:")
        nventa.total = input("Total:")
        self.listaventas.agregarElemento(nventa)
        self.mongo.tryToSave("Tienda","Ventas",self.listaventas.getDict(),"Folio")
        self.listaventas.cargarDatos(self.listaventas.getDict())
        print("Venta creada y agregada a la lista")
        print(nventa)
        self.limpiarPantalla()

    def getClientes(self):
        client = InterfazCliente()
        client.mostrarClientes()
        
    def getProductos(self):
        prod = InterfazProducto()
        prod.mostrarLista()

  

if __name__ == "__main__" :
    x = 1
    interfaz = InterfazVenta()
    while x == 1:
        opcion = interfaz.menuPrincipal()
        if opcion == 1:
            interfaz.agregarVenta()
        elif opcion == 2:
            interfaz.mostrarVentas()
        elif opcion == 3:
            interfaz.eliminarVenta()
        elif opcion == 4:
            interfaz.actualizarVenta()
        elif opcion == 5:
            interfaz.getClientes()
        elif opcion == 6:
            interfaz.getProductos()
        elif opcion == 7:
            print("Cerrando...")
            x = 0
            interfaz.limiarPantalla()
        elif opcion == 8:
            interfaz.verificarContenido()
