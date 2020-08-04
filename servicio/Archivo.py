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
        self.disponibles = puntos
        self.rutas = []

    @staticmethod
    def procesar(archivo):
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

        return Archivo(centros, puntos)

     # Calcula la distancia entre dos puntos (tuplas) con el Teorema de Pitágoras
    @staticmethod
    def distancia_entre(A, B):
        resultado = (((A[0] - B[0]) ** 2) + ((A[1] - B[1]) ** 2))
        resultado = resultado ** (1/2.0)
        return resultado

    # Obtiene el punto más cercano a un punto definido
    def mas_cercano(self, origen, restante):
        primero = True
        menor_distancia = -1
        for punto in self.disponibles:

            distancia_actual = self.distancia_entre(
                origen.coordenadas, punto.coordenadas)
            if ((primero or menor_distancia > distancia_actual) and restante >= punto.productos):
                cercano = punto
                menor_distancia = distancia_actual
                primero = False

        return cercano, menor_distancia

    def avanzar_ruta(self, ruta):
        if (ruta.puede_seguir()):
            siguiente, distancia = self.mas_cercano(
                ruta.punto_actual, ruta.capacidad_restante)
            if (siguiente != None):
                ruta.puntos.append(siguiente)
                ruta.punto_actual = siguiente
                ruta.capacidad_restante -= siguiente.productos
                ruta.distancia_recorrida += distancia

                self.remove_disponible_by_id(siguiente.id)
            else:
                ruta.capacidad_restante = 0

        return ruta

    def remove_disponible_by_id(self, id):
        for disponible in self.disponibles:
            if (disponible.id == id):
                self.disponibles.remove(disponible)

    def construir_rutas(self):
        for centro in self.centros:
            self.rutas.append(Ruta("Camión " + str(centro.id), centro, []))

        while (len(self.disponibles) > 0):
            primero = True
            for ruta in self.rutas:
                if ((primero or ruta_menor.distancia_recorrida > ruta.distancia_recorrida) and ruta.puede_seguir()):

                    ruta_menor = ruta
                    primero = False

            ruta = self.avanzar_ruta(ruta_menor)
