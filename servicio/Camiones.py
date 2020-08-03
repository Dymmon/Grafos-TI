class Estructura_Ordenada:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def mostrar(self):
        print("coordenada X:", self.X)
        print("coordenada Y:", self.Y)


class Camion:
    def __init__(self, centro, ptos, prod):
        self.centro_dist = centro
        self.ptos_venta = ptos
        self.productos = prod

    def mostrar(self):
        print("centro de distribución:", self.centro_dist)
        print("Puntos de venta:", self.ptos_venta)
        print("Productos disponibles:", self.productos)


def leer_archivo():
    f = open("instrucciones.txt", "r")
    lista = []
    centros = []
    puntos = []
    for i in f:
        lista.append(i)
    i = 0
    while (i < len(lista)):
        if (lista[i][0] == "C"):
            j = 2
            aux = ""
            while (j < len(lista[i])):
                if (lista[i][j] > chr(47) and lista[i][j] < chr(58)):
                    aux += lista[i][j]
                if (lista[i][j] == ";"):
                    while(len(centros)-1 < int(aux)):
                        centros.append(None)
                    indi = int(aux)
                    aux = ""
                if (lista[i][j] == ","):
                    x_c = int(aux)
                    aux = ""
                if (lista[i][j] == '\n'or j == len(lista[i])-1):
                    centros[indi] = (x_c, int(aux))
                    j = len(lista[i])
                j += 1
        if (lista[i][0] == "P"):
            j = 2
            aux = ""
            while (j < len(lista[i])):
                if (lista[i][j] > chr(47) and lista[i][j] < chr(58)):
                    aux += lista[i][j]
                if (lista[i][j] == ";"):
                    while (len(puntos)-1 < int(aux)):
                        puntos.append(None)
                    indice = int(aux)
                    aux = ""
                if (lista[i][j] == ","):
                    x = int(aux)
                    aux = ""
                if (lista[i][j] == '\n' or j == len(lista[i])-1):
                    puntos[indice] = (x, int(aux))
                    j = len(lista[i])
                j += 1

        i += 1
    return centros, puntos


def buscar_id(centros, cent):
    i = 0
    while(i < len(centros)):
        if(centros[i] == cent):
            return i
        i += 1


def distancia(A, B):
    aux = (((A[0]-B[0])*(A[0]-B[0])) + ((A[1]-B[1])*(A[1]-B[1])))
    aux = aux**(1/2.0)
    return aux


def mas_cercano(inicio, recorridos, puntos):
    first = True
    i = 0
    while(i < len(puntos)):
        if(not first and aux > distancia(inicio, puntos[i]) and (puntos[i] not in recorridos)):
            aux = (distancia(inicio, puntos[i]))
            siguiente = puntos[i]
        if(first):
            aux = (distancia(inicio, puntos[i]))
            siguiente = puntos[i]
            first = False
        i += 1
    recorridos.append(siguiente)
    return siguiente


def crear_ruta(camion, centros, puntos):
    # Técnica matemática "Programación dinámica"
    orden = []
    recorridos = []
    orden.append("Centro de distribucion " +
                 str(buscar_id(centros, camion.centro_dist)))
    orden.append("punto de venta " + str(buscar_id(puntos,
                                                   mas_cercano(camion.centro_dist, recorridos, camion.ptos_venta))))
    while(len(recorridos) < len(camion.ptos_venta)):
        orden.append("Punto de venta " + str(buscar_id(puntos, mas_cercano(
            recorridos[len(recorridos)-1], recorridos, camion.ptos_venta))))
    orden.append("A mimir señor camion")
    # no se que hacer con los productos we, aiura
