from PuntoVenta import PuntoVenta
from utils import debug_print

ARCHIVO = "Ruta"


class Ruta:
    def __init__(self, camion, centro, puntos):
        debug_print(ARCHIVO, "__init__", str(
            {"camion": camion, "centro": centro, "puntos": puntos}))
        self.camion = camion
        self.centro = centro
        self.puntos = puntos

    # Calcula la cantidad de productos entregados en esta ruta
    def cantidad_productos(self):
        suma = 0
        for punto in self.puntos:
            suma += punto.productos
        return suma

    # Convierte el objeto en un diccionario
    def to_dict(self):
        return {
            "camion": self.camion,
            "centroDistribucion": self.centro.id,
            "productos": self.cantidad_productos(),
            "ruta": [self.centro.to_dict()] + PuntoVenta.lista_to_dict(self.puntos)
        }

    # Convierte una lista de objetos en una lista de diccionarios
    @staticmethod
    def lista_to_dict(rutas):
        lista = []
        for ruta in rutas:
            print(ruta.to_dict())
            lista.append(ruta.to_dict())
        return lista

    # Obtiene un objeto por ID desde una lista de objetos
    @staticmethod
    def get_by_id(id, centros):
        for centro in centros:
            if (centro.id == id):
                return centro
        return None

    # Calcula la distancia entre dos puntos (tuplas) con el Teorema de Pitágoras
    @staticmethod
    def distancia_entre(A, B):
        resultado = (((A[0] - B[0]) ** 2) + ((A[1] - B[1]) ** 2))
        resultado = resultado ** (1/2.0)
        return resultado

    # Calcula la distancia total en una ruta
    @staticmethod
    def distancia_total(puntos):
        recorridos = []
        recorridos.append(puntos)
        total = 0

        for punto in puntos:
            total += Ruta.distancia_entre(recorridos[-1].coordenadas,
                                          punto.coordenadas)
            recorridos.append(punto)

        return total

    # Obtiene el punto más cercano a un punto definido
    @staticmethod
    def mas_cercano(inicial, puntos, recorridos=[]):
        primero = True
        for punto in puntos:
            nueva_distancia = Ruta.distancia_entre(inicial, punto.coordenadas)
            if (primero or (menor > nueva_distancia and (punto not in recorridos))):
                siguiente = punto
                menor = nueva_distancia

            primero = False

        if (siguiente not in recorridos):
            recorridos.append(siguiente)
        return siguiente

    @staticmethod
    def candidato(inicio, disponibles, maximo):
        orden = [inicio]
        recorridos = [inicio]

        cantidad = inicio.productos
        disponibles_actual = []

        for disponible in disponibles:
            if (disponible not in recorridos):
                disponibles_actual.append(disponible)

        while (cantidad < maximo):
            cercano = Ruta.mas_cercano(
                recorridos[-1], disponibles_actual, recorridos)
            if (cercano != None):
                cantidad += recorridos[-1].productos
            else:
                cantidad += maximo
            if (cantidad <= maximo):
                if (cercano not in orden):
                    orden.append(cercano)

                disponibles_actual = []
                for disponible in disponibles:
                    if (disponible not in recorridos):
                        disponibles_actual.append(disponible)

        a = Ruta.distancia_total(orden)
        return orden, a

    @staticmethod
    def seleccion_pv(maximo, puntos, recorridos):
        disponibles = []
        for punto in puntos:
            if (punto not in recorridos and punto != None):
                disponibles.append(punto)
        if (disponibles == []):
            return None

        primero = True
        ruta = []
        largo = 0

        for disponible in disponibles:
            ruta_actual = []
            largo_actual = 0
            ruta_actual, largo_actual = Ruta.candidato(
                disponible, disponibles, maximo)
            if (primero or largo_actual > largo):
                ruta = ruta_actual
                largo = largo_actual

        return ruta


def crear_ruta(self):
    # Técnica matemática "Programación dinámica"
    '''camion, centros, cant_puntos, recorridos, puntos
    self.puntos = seleccion_pv(camion.productos, recorridos, cant_puntos)
    orden = []
    orden.append("Centro de distribucion " +
                 str(buscar_id(centros, camion.centro_dist)))
    i = 0
    while (i < len(camion.ptos_venta)):
        orden.append("Punto de venta " +
                     str(buscar_id(puntos, camion.ptos_venta[i])))
        i += 1
    orden.append("A mimir señor camion")
    '''
