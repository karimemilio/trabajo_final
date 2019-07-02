#!/usr/bin/env python
# -*- coding: utf-8 -*-
import modulos
import PySimpleGUI as sg

def main():
	"""Este es el módulo principal que llama a las funciones para cargar los datos y comenzar el juego"""
	palabras, config  = modulos.cargarInfo()
	# palabras = {'J': [{'palabra': 'blanco'},{'palabra': 'azul'}], 'N': [{'palabra': 'negro'}], 'B': [{'palabra': 'correr'}]}
	# config = {'J': {'cantidad': 1, 'color': 'red'}, 'N': {'cantidad': 1, 'color': 'white'}, 'B': {'cantidad': 1, 'color': 'yellow'}, 'mayuscula': False, 'horizontal': True}
	if not palabras:
		sg.PopupError('No se le cargaron datos al Diccionario')
	else:
		modulos.jugar(palabras, config)

if __name__ == '__main__':
		main()
