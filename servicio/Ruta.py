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

    def cantidad_productos(self):
        suma = 0
        for punto in self.puntos:
            suma += punto.productos
        return suma

    def to_dict(self):
        return {
            "camion": self.camion,
            "centroDistribucion": self.centro.id,
            "productos": self.cantidad_productos(),
            "ruta": [self.centro.to_dict()] + PuntoVenta.lista_to_dict(self.puntos)
        }

    @staticmethod
    def lista_to_dict(rutas):
        lista = []
        for ruta in rutas:
            print(ruta.to_dict())
            lista.append(ruta.to_dict())
        return lista

    @staticmethod
    def get_by_id(id, centros):
        for centro in centros:
            if (centro.id == id):
                return centro
        return None
