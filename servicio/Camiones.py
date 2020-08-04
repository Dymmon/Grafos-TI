
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


def dist_total(camino):
    i = 1
    recorridos = []
    recorridos.append(camino[0])
    total = 0
    while(i < len(camino)):
        total += distancia(recorridos[i-1], camino[i])
        recorridos.append(camino[i])
        i += 1
    return total


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
    if(siguiente not in recorridos):
        recorridos.append(siguiente)
    return siguiente


def candidato(disponibles, maximo, inicio):
    orden = []
    recorridos = []
    orden.append(inicio)
    recorridos.append(inicio)
    cant = inicio[2]
    disp = []
    i = 0
    while(i < len(disponibles)):
        if(disponibles[i] not in recorridos):
            disp.append(disponibles[i])
        i += 1
    while(cant < maximo):
        a = mas_cercano(recorridos[len(recorridos)-1], recorridos, disp)
        if(a != None):
            cant += recorridos[len(recorridos)-1][2]
        if(a == None):
            cant += maximo
        if(cant <= maximo):
            if(a not in orden):
                orden.append(a)
            i = 0
            disp = []
            while(i < len(disponibles)):
                if(disponibles[i] not in recorridos):
                    disp.append(disponibles[i])
                i += 1
    a = dist_total(orden)
    return orden, a


def seleccion_pv(maximo, recorridos, puntos_venta):
    disponibles = []
    for i in puntos_venta:
        if(i not in recorridos and i != None):
            disponibles.append(i)
    if(disponibles == []):
        return None
    i = 0
    aux_ruta = []
    aux_largo = 0
    first = True
    ruta = []
    largo = 0
    while(i < len(disponibles)):
        aux_ruta, aux_largo = candidato(disponibles, maximo, disponibles[i])
        if(not first and aux_largo > largo):
            ruta = aux_ruta
            largo = aux_largo
        if(first):
            ruta = aux_ruta
            largo = aux_largo
        i += 1
    return ruta


def buscar_id(centros, cent):
    i = 0
    while(i < len(centros)):
        if(centros[i] != None):
            if(centros[i][0] == cent[0] and centros[i][1] == cent[1]):
                return i
        i += 1


def distancia(A, B):
    aux = (((A[0]-B[0])*(A[0]-B[0])) + ((A[1]-B[1])*(A[1]-B[1])))
    aux = aux**(1/2.0)
    return aux


def crear_ruta(camion, centros, cant_puntos, recorridos, puntos):
    # Técnica matemática "Programación dinámica"
    camion.ptos_venta = seleccion_pv(camion.productos, recorridos, cant_puntos)
    orden = []
    orden.append("Centro de distribucion " +
                 str(buscar_id(centros, camion.centro_dist)))
    i = 0
    while(i < len(camion.ptos_venta)):
        orden.append("Punto de venta " +
                     str(buscar_id(puntos, camion.ptos_venta[i])))
        i += 1
    orden.append("A mimir señor camion")
