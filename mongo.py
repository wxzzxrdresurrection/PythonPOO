import pymongo
from jsonClass import JSONConvert
from productos import Producto
from clientes import Cliente
from ventas import Venta
import os

class MongoConnection(JSONConvert):

    def __init__(self):
        self.cadena = 'mongodb+srv://wizzard:Luis200315@cluster0.gbgv62y.mongodb.net/?retryWrites=true&w=majority'
        self.listaprod = Producto()
        #self.listaprod.getObjfromList("ProductosPendientes")
        self.listaclientes = Cliente()
        #self.listaclientes.getObjfromList("ClientesPendientes")
        self.listaventa = Venta()
        #self.listaventa.getObjfromList("VentasPendientes")

    def testConnection(self):
        try:
            myclient = pymongo.MongoClient(self.cadena)
            print("Conexion exitosa")
            return myclient
        except:
            print("Error de conexion")
            return None
        

    def tryToSave(self,nombreDB,nombreColl,dataEnJson,elemento):    
            con = self.testConnection()
            if con != None:
                db = con[nombreDB]
                coleccion = db[nombreColl]
                datosDB = coleccion.find()
                lista=[]
                print("creando lista")
                for datos in datosDB:
                    lista.append(datos)
                if self.verificarContenido(nombreColl+"Pendientes") != 0:
                    arch = self.leerJSON(nombreColl+"Pendientes.json")
                    coleccion.insert_many(arch)
                    if nombreColl == "Ventas":
                        self.listaventa.listageneral.clear()
                    if nombreColl == "Productos":
                        self.listaprod.listageneral.clear()
                    if nombreColl == "Clientes":
                        self.listaclientes.listageneral.clear()
                    os.remove(nombreColl+"Pendientes.json")
                if len(lista)==0:
                    coleccion.insert_many(dataEnJson)
                else:
                    coleccion.insert_one(elemento.getDict())
            else:
                self.guardarEnLista(nombreColl,elemento)

    def guardarEnLista(self,archivo,elemento):
        if archivo == "Ventas":
            self.listaventa.agregarElemento(elemento)
            self.cargarJSON(self.listaventa.getDict(),archivo+"Pendientes")
        if archivo == "Productos":
            self.listaprod.agregarElemento(elemento)
            self.cargarJSON(self.listaprod.getDict(),archivo+"Pendientes")
        if archivo == "Clientes":
            self.listaclientes.agregarElemento(elemento)
            self.cargarJSON(self.listaclientes.getDict(),archivo+"Pendientes")
        

        
        
if __name__ == "__main__":
    Mongo = MongoConnection()
    con = Mongo.testConnection()
    
    
    
    