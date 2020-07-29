class Estructura_Ordenada:
    def __init__(self,x,y):
        self.X=x
        self.Y=y
    def mostrar(self):
        print("coordenada X:",self.X)
        print("coordenada Y:",self.Y)

class Camion:
    def __init__(self):
        self.centro_dist
        self.ptos_venta=[]
        self.recorrido
        self.productos
        
    def mostrar(self):
        print("centro de distribución:",self.centro_dist)
        print("Puntos de venta:", self.ptos_venta)
        print("Productos disponibles:",self.productos)

def leer_archivo():
    f=open("instrucciones.txt", "r")
    lista=[]
    centros=[]
    puntos=[]
    for i in f:
        lista.append(i)
    i=0
    while(i<len(lista)):
        if(lista[i][0]=="C"):
            j=2
            aux=""
            while(j<len(lista[i])):
                if(lista[i][j]>chr(47) and lista[i][j]< chr(58)):
                    aux+=lista[i][j]
                if(lista[i][j] == ";"):
                    while(len(centros)-1<int(aux)):
                        centros.append(None)
                    indi=int(aux)
                    aux=""
                if(lista[i][j] == ","):
                    x_c=int(aux)
                    aux=""
                if(lista[i][j] == '\n'or j == len(lista[i])-1):
                    centros[indi]=(x_c,int(aux))
                    j=len(lista[i])
                j+=1
        if(lista[i][0]=="P"):
            j=2
            aux=""
            while(j<len(lista[i])):
                if(lista[i][j]>chr(47) and lista[i][j]< chr(58)):
                    aux+=lista[i][j]
                if(lista[i][j] == ";"):
                    while(len(puntos)-1<int(aux)):
                        puntos.append(None)
                    indice=int(aux)
                    aux=""
                if(lista[i][j] == ","):
                    x=int(aux)
                    aux=""
                if(lista[i][j] == '\n' or j == len(lista[i])-1):
                    puntos[indice]=(x,int(aux))
                    j=len(lista[i])
                j+=1

        i+=1
    return centros,puntos
    
