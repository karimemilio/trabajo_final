#!/usr/bin/env python
# -*- coding: utf-8 -*-
import modulos
import PySimpleGUI as sg

def main():
	#palabras, config  = modulos.cargarInfo()
	config = {'J': {'cantidad': 1, 'color': 'red'}, 'N': {'cantidad': 1, 'color': 'yellow'}, 'B': {'cantidad': 1, 'color': 'green'}, 'mayuscula': False, 'Horizontal': False, 'ayuda': True}
	palabras = {'J': [{'palabra': 'blanco', 'descripcion': 'color clarito'}], 'N': [{'palabra': 'cerveza', 'descripcion': 'una rica bebida'}, {'palabra': 'negro', 'descripcion': 'color de los africanos '}], 'B': [{'palabra': 'correr', 'descripcion': 'troti rapidito rapidito”)'}, {'palabra': 'caminar', 'descripcion': 'lento lento como una tortuga'}]}or esVacio(dicc)
	if config == None:
		print('Fin de la ejecucion')
	else:
		modulos.jugar(palabras,config)

if __name__ == '__main__':
		main()
