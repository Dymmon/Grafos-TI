from datetime import datetime


def fecha_y_hora():
    return '--> '+str(datetime.now(tz=None).replace(microsecond=0))+': '


def debug_print(archivo, funcion, extra=""):
    string = fecha_y_hora() + "[" + archivo + ".py] " + funcion + "()"
    print(string)
    print(extra)
    return string
