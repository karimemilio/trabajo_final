#!/usr/bin/env python
# -*- coding: utf-8 -*-
import modulos
import PySimpleGUI as sg

def main():
	palabras, config  = modulos.cargarInfo()
	#print(palabras, config)
	if not palabras:
		sg.PopupError('No se le cargaron datos al Diccionario')
	else:
		modulos.jugar(palabras, config)

if __name__ == '__main__':
		main()
