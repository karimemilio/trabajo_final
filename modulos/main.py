#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	El modulo main es el encargado de llamar primero a la funcion Modulos, y cargar toda la informacion necesaria para el armado
	de la sopa de letra. Luego invocar el modulo jugar, para proceder a la inicializacion del juego"""

import modulos
import PySimpleGUI as sg
def main():
	palabras, config  = modulos.cargarInfo()
	if config == None:
		print('Fin de la ejecucion')
	else:
		modulos.jugar(palabras,config)

if __name__ == '__main__':
		main()
