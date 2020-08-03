from utils import debug_print

ARCHIVO = "PuntosVenta"


class Estructura:
    def __init__(self, centros, puntos):
        debug_print(ARCHIVO, "__init__", str(
            {"centros": centros, "puntos": puntos}))
        self.centros = centros
        self.puntos = puntos
