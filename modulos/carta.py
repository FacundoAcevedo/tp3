#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       carta.py
"""Modulo donde habita la clase carta"""

class Carta(object):
    """Clase carta"""
    def __init__(self, nombre, norte, sur, este, oeste, dueno):
        """Constructor"""
        self.nombre = nombre
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste
        self.dueno = dueno
        
    def dueno(self, dueno):
        """Define al dueño de la carta"""
        #  @param dueño
        #  @return string / None
        self.dueno = dueno
        
    def __str__(self):
        """string"""
        return """ ***
        Nombre: %s
        Fuerza: %s,%s,%s,%s
        Dueño: %s""" % (self.nombre, self.norte, self.sur, self.este,\
                        self.oeste, self.dueno)
    
        
