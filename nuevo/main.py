#!/usr/bin/env python
# -*- coding: utf-8 -*-
import modulos
import jugar
import PySimpleGUI as sg

def main():
	"""	Módulo principal de la aplicación.
	Dirige los eventos: Llama a los módulos de carga de palabras y configuración y arma la matriz de juego"""

	#config = {'J': {'cantidad': 1, 'color': 'red'}, 'N': {'cantidad': 1, 'color': 'yellow'}, 'B': {'cantidad': 1, 'color': 'green'}, 'mayuscula': False, 'Horizontal': False, 'ayuda': True}
	#palabras = {'J': [{'palabra': 'blanco', 'descripcion': 'color clarito'}], 'N': [{'palabra': 'cerveza', 'descripcion': 'una rica bebida'}, {'palabra': 'negro', 'descripcion': 'color de los africanos '}], 'B': [{'palabra': 'correr', 'descripcion': 'troti rapidito rapidito”)'}, {'palabra': 'caminar', 'descripcion': 'lento lento como una tortuga'}]}or esVacio(dicc)
	print('Notas de programación: ')

	palabras, config  = modulos.cargarInfo()	#Obtiene el diccionario de palabras y el diccionario de configuración
	if config == None:							#Controla que se hayan ingresado datos para continuar el procesamiento o finalizar la ejecución
		sg.PopupError('Se decidio no jugar')
	else:
		jugar.jugar(palabras, config)			#Invoca al módulo jugar que arma la matriz del juego
	print('Fin de la ejecucion')

if __name__ == '__main__':						#Esta condición se cumple si el módulo no es importado
		main()

