import lista as Lista
import clientes
import productos
import clientes

class Venta(Lista.Lista):

    def __init__(self, folio="NF",cliente="sincliente", detalles_producto="SIN PRODUCTOS", fecha="SIN FECHA", total=0):
        self.folio = folio
        self.cliente = cliente
        self.detalles_producto = detalles_producto
        self.fecha = fecha
        self.total = total
        super().__init__()

    def __str__(self):
        return f"Folio: {self.folio} Cliente: {self.cliente}, Detalles producto: {self.detalles_producto}, Fecha: {self.fecha}, Total: {self.total}"
    
    def cargarDatos(self,lista,nombre="ventas2"):
        data = self.cargarJSON(lista,nombre)
        return data

    def leerDatos(self,archivo):
        return self.leerJSON(archivo+".json")

    def getListProd(self,nlista):
        lista = []
        for p in nlista:
            lista.append(productos.Producto(p["Codigo"],p["Nombre"],p["Descripcion"],p["Precio"]))
        return lista

    def getDictToProd(self,lista):
        prod = productos.Producto()
        for p in lista:
            prod.agregarElemento(p)
        return prod

    def getDict(self):
        arreglo = []
        if (len(self.listageneral)>0):
            for v in self.listageneral:
                arreglo.append(v.getDict())
            return arreglo
        else:
            return {"Folio": self.folio ,"Cliente": self.cliente.getDict(), "Detalle productos": self.detalles_producto.getDict(), "Fecha": self.fecha, "Total": self.total}

    def getObjfromList(self,archivo):
        data = self.leerDatos(archivo)
        for v in data:
            cliente = clientes.Cliente(v["Cliente"]["RFC"],v["Cliente"]["Nombre"],v["Cliente"]["Telefono"])
            prod = productos.Producto()
            for p in v["Detalle productos"]:
                prod.agregarElemento(productos.Producto(p["Codigo"],p["Nombre"],p["Descripcion"],p["Precio"]))
            self.listageneral.append(Venta(v["Folio"],cliente,prod,v["Fecha"],v["Total"]))
        return self.listageneral

    
if __name__ == "__main__":
    cliente = clientes.Cliente("ZAZL030815RJ2","Luis Zapata","8713530073")
    producto =productos.Producto(1,"Coca Cola","Bebida gaseosa",12.50)
    producto1 = productos.Producto(2,"Agua","Bebida",10)
    listaprod = productos.Producto()
    listaprod.agregarElemento(producto)
    listaprod.agregarElemento(producto1)

    venta1 = Venta(1,cliente,listaprod,"2022-01-01",200)
    #venta1.cargarDatos(venta1.getDict(),"ventas2")
    listaVentas = Venta()
    listaVentas.agregarElemento(venta1)
    listaVentas.cargarDatos(listaVentas.getDict(),"ventas2")




    


