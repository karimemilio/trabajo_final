#!/usr/bin/env python
# -*- coding: utf-8 -*-
import modulos
import PySimpleGUI as sg

def main():
	palabras, config  = modulos.cargarInfo()
	print('--------------palabras--------------')
	print(palabras)
	print ('---------------------COONFIGURACION--------------')
	print (config)
	if config == None:
		print('Fin de la ejecucion')
	else:
		modulos.jugar(palabras,config)

if __name__ == '__main__':
		main()
