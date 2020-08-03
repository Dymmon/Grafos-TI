from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from servicios import leer_y_procesar_archivo, obtener_hoja_de_ruta
from utils import debug_print

application = Flask(__name__)
cors = CORS(application, resources={
            r"/*": {"resources": ["http://localhost:8080", "http://localhost:8081"]}})
application.config['CORS_HEADERS'] = 'Content-Type'

ARCHIVO = "api"
EXTENSIONES_PERMITIDAS = ["txt"]


def extension_permitida(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in EXTENSIONES_PERMITIDAS


@application.route('/', methods=['GET'])
def conectar():
    debug_print("api", "conectar")
    return jsonify(mensaje='Conectado a servicio')


@application.route('/resumen', methods=['POST'])
def resumen():
    debug_print(ARCHIVO, "resumen")

    if 'archivo' not in request.files:
        debug_print(ARCHIVO, "resumen",
                    "No se encontró el archivo")
        return jsonify(error='No se encontró el archivo')
    else:
        archivo = request.files['archivo']

        if archivo.filename == '':
            debug_print(ARCHIVO, "resumen",
                        "No se cargó ningún archivo")
            return jsonify(error='No se cargó ningún archivo')
        if not extension_permitida(archivo.filename):
            debug_print(ARCHIVO, "resumen",
                        "Extensión de archivo no permitida")
            return jsonify(error="Extensión de archivo no permitida")
        return leer_y_procesar_archivo(archivo.read().decode("utf-8"))


@application.route('/rutas', methods=['POST'])
def rutas():
    debug_print(ARCHIVO, "rutas")
    content = request.get_json(silent=True)
    return obtener_hoja_de_ruta(content)


if __name__ == '__main__':
    application.run(debug=True, host='localhost', port=5151)
