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
        self.capacidad_restante = 1000
        self.distancia_recorrida = 0
        self.punto_actual = centro

    # Calcula la cantidad de productos entregados en esta ruta

    def cantidad_productos(self):
        suma = 0
        for punto in self.puntos:
            suma += punto.productos
        return suma

    def puede_seguir(self):
        return self.capacidad_restante > 0

    # Convierte el objeto en un diccionario
    def to_dict(self):
        return {
            "camion": self.camion,
            "capacidadRestante": self.capacidad_restante,
            "distanciaRecorrida": self.distancia_recorrida,
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
