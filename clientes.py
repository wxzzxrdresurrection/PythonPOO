import lista as Lista

class Cliente(Lista.Lista):
    def __init__(self,rfc="Sin RFC",nombre="Sin nombre",telefono="Sin telefono"):
        self.rfc = rfc
        self.nombre = nombre
        self.telefono = telefono
        super().__init__()
    
    def __str__(self):
        if len(self.listageneral)>0:
            return f"La lista contiene: {len(self.listageneral)} clientes"
        else:
            return f"RFC: {self.rfc} Nombre: {self.nombre} Telefono: {self.telefono}"

    def getDict(self):
        arreglo = []
        if (len(self.listageneral)>0):
            for c in self.listageneral:
                arreglo.append(c.getDict())
            return arreglo
        else:
            return {"RFC": self.rfc, "Nombre": self.nombre, "Telefono": self.telefono}

    def cargarDatos(self,lista,nombre="lista de clientes"):
        data = self.cargarJSON(lista,nombre)
        return data

    def leerDatos(self,archivo):
        return self.leerJSON(archivo+".json")

    def getObjfromList(self,archivo):
        data = self.leerDatos(archivo)
        for c in data:
            self.listageneral.append(Cliente(c["RFC"],c["Nombre"],c["Telefono"]))
        return self.listageneral

if __name__ == "__main__":
    lista = Cliente()
    cliente1 = Cliente("ZAZL030815RJ2","Luis Zapata","8713530073")
    cliente2 = Cliente("ZUOA7509131L7","Angeles Zuniga","8713263563")
    cliente3 = Cliente("RECJ030607HJ3","Javier Resendiz","8711228330")
    lista.agregarElemento(cliente1)
    lista.agregarElemento(cliente2)
    lista.agregarElemento(cliente3)

    lista.cargarDatos(lista.getDict(),"lista de clientes")

    lista.getObjfromList()
    print(lista)



    
    
    



