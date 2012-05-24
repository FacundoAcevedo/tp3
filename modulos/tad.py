#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       tad.py
#version 0.1
"""Modulo. Contiene los tipos abstractos de datos a usar
en el programa"""

class Pila(object):
    """Clase pila"""
    def __init__(self):
        """Constructor"""
        self.items = []
        self.largo = 0
    def __str__(self):
        """string"""
        return str(self.items)
    def __len__(self):
        """len"""
        return str(self.largo)
    def agregar(self,item):
        """Agrega un objeto a la pila"""
        self.items.append(item)
        self.largo += 1
    def liberar(self):
        """Quita elemento de la pila"""
        try:
            self.largo -= 1
            return self.items.pop()
        except:
            return None
        
    def estaVacia(self):
        """True si esta vacia, de lo contrario False"""
        return (self.items == [])


class Cola(object):
    """Clase cola"""
    def __init__(self):
        """Constructor"""
        self.items = []
        self.largo = 0
    def __str__(self):
        """string"""
        return str(self.items)
    def __len__(self):
        """len"""
        return str(self.largo)
    def agregar(self,item):
        """Agrega un objeto al principio de la cola"""
        self.items.insert(0, item)
        self.largo += 1
    def liberar(self):
        """Quita el primer elemento de la cola"""
        try:
            self.largo -= 1
            return self.items.pop()
        except:
            return None
    def estaVacia(self):
        """True si esta vacia, de lo contrario False"""
        return (self.items == [])

class ListaSimplementeEnlazada(object):
    pass
    
class Nodo(object):
    pass
    
