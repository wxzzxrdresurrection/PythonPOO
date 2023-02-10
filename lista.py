import jsonClass

class Lista(jsonClass.JSONConvert):

    def __init__(self):
        self.listageneral = []

    def __str__ (self):
        return f"Contenido de la lista:{self.listageneral}"

    def agregarElemento(self,elemento):
        self.listageneral.append(elemento)
    
    def eliminarElemento(self,elemento):
        self.listageneral.remove(elemento)

    def mostrarElementos(self):
        return self.listageneral
        

