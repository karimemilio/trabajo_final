#!/usr/bin/env python
# -*- coding: utf-8 -*-
import modulos
import PySimpleGUI as sg

def main():
<<<<<<< HEAD
	palabras, config  = modulos.cargarInfo()
	print('--------------palabras--------------')
	print(palabras)
	print ('---------------------COONFIGURACION--------------')
	print (config)
	if config == None:
		print('Fin de la ejecucion')
=======
	"""Este es el módulo principal que llama a las funciones para cargar los datos y comenzar el juego"""
	palabras, config  = modulos.cargarInfo()
	# palabras = {'J': [{'palabra': 'blanco'},{'palabra': 'azul'}], 'N': [{'palabra': 'negro'}], 'B': [{'palabra': 'correr'}]}
	# config = {'J': {'cantidad': 1, 'color': 'red'}, 'N': {'cantidad': 1, 'color': 'white'}, 'B': {'cantidad': 1, 'color': 'yellow'}, 'mayuscula': False, 'horizontal': True}
	if not palabras:
		sg.PopupError('No se le cargaron datos al Diccionario')
>>>>>>> 0422f448a8c2db6ca43b7bb270ceaf388fa12cf0
	else:
		modulos.jugar(palabras,config)

if __name__ == '__main__':
		main()
