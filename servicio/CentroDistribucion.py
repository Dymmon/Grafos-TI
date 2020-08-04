from utils import debug_print

ARCHIVO = "CentroDistribucion"


class CentroDistribucion:
    def __init__(self, id, coordenadas):
        debug_print(ARCHIVO, "__init__", str(
            {"id": id, "coordenadas": coordenadas}))
        self.id = id
        self.coordenadas = coordenadas

    @staticmethod
    def from_json(json):
        debug_print(ARCHIVO, "from_json", json)
        return CentroDistribucion(json["id"], (json["coordenadas"]["x"], json["coordenadas"]["y"]))

    def to_dict(self):
        debug_print(ARCHIVO, "to_dict")
        return {
            "id": self.id,
            "esCentroDistribucion": True,
            "coordenadas": {
                "x": self.coordenadas[0],
                "y": self.coordenadas[0],
            },
            "productos": None,
        }

    @staticmethod
    def lista_to_dict(centros):
        debug_print(ARCHIVO, "lista_to_dict", {"centros": centros})
        lista = []
        for centro in centros:
            lista.append(centro.to_dict())
        return lista

    @staticmethod
    def get_by_id(id, centros):
        debug_print(ARCHIVO, "get_by_id", {"id": id, "centros": centros})
        for centro in centros:
            if (centro.id == id):
                return centro
        return None
