#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	El modulo main es el encargado de llamar primero a la funcion Modulos, y cargar toda la informacion necesaria para el armado
	de la sopa de letra. Luego invocar el modulo jugar, para proceder a la inicializacion del juego"""

import modulos
import jugar
import PySimpleGUI as sg

def main():
	palabras, config  = modulos.cargarInfo()
	if config == None:
		sg.PopupAutoClose('Fin de la ejecución', button_color=('black','#AEA79F'),background_color='#b3d4fc', title=':(')
	else:
		jugar.jugar(palabras,config)

if __name__ == '__main__':
		main()
