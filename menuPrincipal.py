from menuClientes import InterfazCliente
from menuProductos import InterfazProducto
from menuVentas import InterfazVenta


class Principal:
    def __init__(self):
        self.interfazVenta = InterfazVenta()
        self.interfazCliente = InterfazCliente()
        self.interfazProducto = InterfazProducto()

if __name__ == "__main__":
    principal = Principal()
    while True:
        print("Menu principal")
        print("1.- Ventas")
        print("2.- Clientes")
        print("3.- Productos")
        print("4.- Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            principal.interfazVenta.menuPrincipal()
        elif opcion == 2:
            principal.interfazCliente.menuPrincipal()
        elif opcion == 3:
            principal.interfazProducto.Inicio()
        elif opcion == 4:
            break
        else:
            print("Opcion invalida")