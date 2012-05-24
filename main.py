#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       main.py
#       

###importacion de modulos
import sys
import os
#importo por funcion
#ejemplo: tad = importar("modulos/tad.py")



def importar(ruta_a_modulo):
    """importa modulos por nombre de archivo"""
    
    directorio, modulo_nombre = os.path.split(ruta_a_modulo)
    modulo_nombre = os.path.splitext(modulo_nombre)[0]
    #obtiene la ruta sin extension    
    ruta = list(sys.path)
    sys.path.insert(0, directorio)
    #agrega la ruta para poder importar los modulos
    try:
        return __import__(modulo_nombre)
    finally:
        sys.path[:] = ruta # restaurar
    



