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

    return jsonify({
        "puntosVenta": PuntoVenta.lista_to_dict(procesado.puntos),
        "centrosDistribucion": CentroDistribucion.lista_to_dict(procesado.centros)
    })


def obtener_hoja_de_ruta(json):
    debug_print(ARCHIVO, "obtener_hoja_de_ruta", str(json))

    centros = []
    puntos = []

    for centro in json["centrosDistribucion"]:
        centros.append(CentroDistribucion.from_json(centro))

    for punto in json["puntosVenta"]:
        puntos.append(PuntoVenta.from_json(punto))

    procesado = Archivo(centros, puntos)
    procesado.construir_rutas()

    return jsonify({
        "rutas": Ruta.lista_to_dict(procesado.rutas)
    })
