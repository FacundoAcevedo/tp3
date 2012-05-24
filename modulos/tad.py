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
	" Modela una lista enlazada, compuesta de Nodos. "
	def __init__(self):
		""" Crea una lista enlazada vacía. """
		# prim: apuntará al primer nodo - None con la lista vacía
		self.prim = None
		# len: longitud de la lista - 0 con la lista vacía
		self.len = 0
	def agregar(self,dato):
		nodo=Nodo(dato,self.prim) #crea un nuevo nodo con el dato como parámetro
		self.prim=nodo   #cambia la referencia self.prim y hace que apunte al nodo creado 
		self.len+=1 
	def pop(self, i = None):
		""" Elimina el nodo de la posición i, y devuelve el dato contenido.
		Si i está fuera de rango, se levanta la excepción IndexError.
		Si no se recibe la posición, devuelve el último elemento. """
		# Verificación de los límites
		if (i < 0) or (i >= self.len):
			raise IndexError("Índice fuera de rango")
		# Si no se recibió i, se devuelve el último.
		if i == None:
			i = self.len - 1
		# Caso particular, si es el primero,
		# hay que saltear la cabecera de la lista
		if i == 0:
			dato = self.prim.dato
			self.prim = self.prim.prox
		# Para todos los demás elementos, busca la posición
		else:
			n_ant = self.prim
			n_act = n_ant.prox
			for pos in xrange(1, i):
				n_ant = n_act
				n_act = n_ant.prox
				# Guarda el dato y elimina el nodo a borrar
				dato = n_act.dato
				n_ant.prox = n_act.prox
			# hay que restar 1 de len
			self.len -= 1
			# y devolver el valor borrado
			return dato


    def __str__(self):
		nodo = self.prim #comienza la lista
		s= '['
		while nodo != None:
			s= s+ str(nodo)+ ","
			nodo = nodo.prox #pasa al proximo nodo
		s=s+ "]" # cierra la lista
		return s

		
	
	
class Nodo(object):
	def __init__(self, dato=None, prox = None):
		self.dato = dato
		self.prox = prox
	def __str__(self):
		return str(self.dato)
	def verLista(nodo):
		""" Recorre todos los nodos a través de sus enlaces,
		mostrando sus contenidos. """
		# cicla mientras nodo no es None
		while nodo:
			#muestra el dato
			print nodo
			# ahora nodo apunta a nodo.prox
			nodo = nodo.prox
