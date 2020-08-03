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
    def distancia_total(self):
        recorridos = []
        recorridos.append(self.centro)
        total = 0

        for punto in self.puntos:
            total += self.distancia_entre(recorridos[-1].coordenadas,
                                          punto.coordenadas)
            recorridos.append(punto)

        return total

    # Obtiene el punto más cercano a un punto definido
    def mas_cercano(self, inicial, recorridos=[]):
        primero = True
        for punto in self.puntos:
            nueva_distancia = self.distancia_entre(inicial, punto.coordenadas)
            if (primero or (menor > nueva_distancia and (punto not in recorridos))):
                siguiente = punto
                menor = nueva_distancia

            primero = False

        if (siguiente not in recorridos):
            recorridos.append(siguiente)
        return siguiente
