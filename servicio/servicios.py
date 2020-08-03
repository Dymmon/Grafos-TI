from flask import jsonify
from utils import debug_print
from Archivo import Archivo
from PuntoVenta import PuntoVenta
from CentroDistribucion import CentroDistribucion
from Ruta import Ruta

ARCHIVO = "servicios"


def leer_y_procesar_archivo(archivo):
    debug_print(ARCHIVO, "leer_y_procesar_archivo", str(archivo))
    procesado = Archivo.procesar(archivo.split("\n"))

    return jsonify(procesado)


def obtener_hoja_de_ruta(json):
    debug_print(ARCHIVO, "obtener_hoja_de_ruta", str(json))

    puntos1 = []
    puntos1.append(PuntoVenta(3, (34, 72), 400))
    puntos1.append(PuntoVenta(2, (82, 12), 200))

    puntos2 = []
    puntos2.append(PuntoVenta(1, (3, 5), 1000))

    rutas = []
    rutas.append(Ruta("Camion 1", CentroDistribucion(1, (22, 2)), puntos1))
    rutas.append(Ruta("Camion 3", CentroDistribucion(2, (152, 45)), puntos2))

    return jsonify({
        "rutas": Ruta.lista_to_dict(rutas)
    })
