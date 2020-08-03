from flask import jsonify
from utils import debug_print
from Estructura import Estructura

ARCHIVO = "servicios"


def leer_y_procesar_archivo(archivo):
    debug_print(ARCHIVO, "leer_y_procesar_archivo", str(archivo))
    estructura = Estructura.desde_archivo(archivo.split("\n"))
    return jsonify({
        "puntosVenta": [
            {
                "id": 1,
                "coordenadas": {
                    "x": 3,
                    "y": 5,
                }
            },
            {
                "id": 2,
                "coordenadas": {
                    "x": 82,
                    "y": 12,
                }
            },
            {
                "id": 3,
                "coordenadas": {
                    "x": 34,
                    "y": 72,
                }
            }
        ],
        "centrosDistribucion": [
            {
                "id": 1,
                "coordenadas": {
                    "x": 22,
                    "y": 2,
                }
            },
            {
                "id": 2,
                "coordenadas": {
                    "x": 152,
                    "y": 45,
                }
            }
        ]
    })


def obtener_hoja_de_ruta(json):
    debug_print(ARCHIVO, "obtener_hoja_de_ruta", str(json))
    return jsonify({
        "rutas": [
            {
                "camion": "Camión 1",
                "centroDistribucion": 1,
                "productos": 600,
                "ruta": [
                    {
                        "id": 1,
                        "esCentroDistribucion": True,
                        "productos": None,
                        "coordenadas": {
                            "x": 152,
                            "y": 45,
                        }
                    },
                    {
                        "id": 3,
                        "esCentroDistribucion": False,
                        "productos": 400,
                        "coordenadas": {
                            "x": 34,
                            "y": 72,
                        }
                    },
                    {
                        "id": 2,
                        "esCentroDistribucion": False,
                        "productos": 200,
                        "coordenadas": {
                            "x": 82,
                            "y": 12,
                        }
                    },

                ],
            },
            {
                "camion": "Camión 2",
                "productos": 1000,
                "centroDistribucion": 2,
                "ruta": [
                    {
                        "id": 2,
                        "esCentroDistribucion": True,
                        "productos": None,
                        "coordenadas": {
                            "x": 22,
                            "y": 2,
                        }
                    },
                    {
                        "id": 1,
                        "esCentroDistribucion": False,
                        "productos": 1000,
                        "coordenadas": {
                            "x": 3,
                            "y": 5,
                        }
                    }


                ],
            }
        ]

    })
