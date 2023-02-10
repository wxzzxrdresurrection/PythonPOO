import json

class JSONConvert:
    
    def cargarJSON(self,lista,nombre):    
        listaJSON = json.dumps(lista,indent=3)
        f = open(nombre+'.json','w')
        f.write(listaJSON)
        f.close()

    def leerJSON(self,archivo):
        f = open(archivo,'r')
        v = json.loads(f.read())
        return v
    
    def verificarContenido(self,archivo):
        a = open(archivo+".json",'r')
        return len(a.read())
        
if __name__ == "__main__":
    jsonA = JSONConvert()
    

        


       
