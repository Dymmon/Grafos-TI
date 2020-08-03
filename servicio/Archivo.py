from utils import debug_print
from PuntoVenta import PuntoVenta
from CentroDistribucion import CentroDistribucion
from Ruta import Ruta

ARCHIVO = "Archivo"


class Archivo:
    def __init__(self, centros, puntos):
        debug_print(ARCHIVO, "__init__", str(
            {"centros": centros, "puntos": puntos}))
        self.centros = centros
        self.puntos = puntos

    @staticmethod
    def procesar(archivo):
        # f = open("instrucciones.txt", "r")
        centros = []
        puntos = []
        for linea in archivo:
            separada = linea.split(";")
            coordenadas = separada[2].split(",")
            tupla_coordenadas = (int(coordenadas[0]), int(coordenadas[1]))
            if (separada[0] == "C"):
                centros.append(CentroDistribucion(
                    int(separada[1]), tupla_coordenadas))
            elif (separada[0] == "P"):
                puntos.append(PuntoVenta(
                    int(separada[1]), tupla_coordenadas))

        return {
            "puntosVenta": PuntoVenta.lista_to_dict(puntos),
            "centrosDistribucion": CentroDistribucion.lista_to_dict(centros)
        }
