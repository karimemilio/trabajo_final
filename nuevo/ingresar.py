#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pattern.text.es import tag,parse, split
import PySimpleGUI as sg
from wiktionaryparser import WiktionaryParser
import validaciones

def generarPalabras(dicc):
    #Creo el diseño de la ventana
    diseñoPalabras = [[sg.Text('Ingrese una palabra')],
          [sg.Input(do_not_clear=False)],
          [sg.Text(' ', key= 'mensaje',size=(37,1))],
          [sg.Text(' ', key= 'palabras',size=(37,3))],
          [sg.Button('Agregar'), sg.Button('Finalizar'),sg.Button('Eliminar')],
          [sg.Radio('Horizontal', 'RADIO1', default = True ), sg.Radio('Vertical', 'RADIO1')],
          [sg.Checkbox('Ayuda')]]

    #Muestro la ventana
    ventanaPalabras = sg.Window('Sopa de letras',auto_size_text=True,default_element_size=(40, 1)).Layout(diseñoPalabras)

    #Proceso la información
    tiposIngresados=('Adjetivos: ' + str(len(dicc['J'])) + '\n' + 'Sustantivos: ' + str(len(dicc['N'])) + '\n' + 'Verbos: ' + str(len(dicc['B']))) #Inicializo el mensaje a mostrar
    while True:     #Se ingresan palabras hasta que se haga clic en 'Finalizar'
        boton, datos = ventanaPalabras.Read()   #Leo los datos de la ventana
        palabra = datos[0]
        if boton is None or boton == 'Finalizar':
            ventanaPalabras.Close()
            return (dicc, (True if datos[1] else False))
        else:
            try:
                ingreso = validaciones.validar(palabra) #Retorna tupla (bool,tipo,definicion)
                if ingreso[0]:
                    if boton == 'Agregar':
                        lista_palabras = map(lambda item: { item[0] : item[1] }, dicc[ingreso[1]])
                        if palabra in lista_palabras:
                            mensaje='La palabra ya fue ingresada'
                            print("Ya esta en la lista")
                        else:
                            if datos[3]:
                                print("Intenta agregar a la lista")
                                dicc[ingreso[1]].append({ 'palabra': palabra, 'descripcion': ''.join(ingreso[2]) })
                                print("Agrega a la lista con descripcion")
                                print(" ")
                            else:
                                dicc[ingreso[1]].append({ 'palabra': palabra })
                                print("Agrega sin descripcion")
                            mensaje='La palabra ingresada es válida'
                    if boton == 'Eliminar':
                        lista_pal = map(lambda item: item[0], dicc[ingreso[1]])
                        if palabra in lista_pal:
                            dicc[ingreso[1]].remove((palabra,ingreso[2]))
                            mensaje='La palabra se eliminó'
                        else:
                            mensaje='La palabra ingresada no está en la lista'
                else:
                    sg.PopupError('La palabra ingresada no es valida')
                tiposIngresados=('Adjetivos: ' + str(len(dicc['J'])) + '\n' + 'Sustantivos: ' + str(len(dicc['N'])) + '\n' + 'Verbos: ' + str(len(dicc['B'])))
                ventanaPalabras.FindElement('mensaje').Update(mensaje)
                ventanaPalabras.FindElement('palabras').Update(tiposIngresados)

            except:
                print('Ha ocurrido un error')

def seleccion(dicc):
    cant = {}
    for tipo in dicc:
        cant[tipo] = []
        for i in range(len(dicc[tipo])):
            cant[tipo].append(i+1)
    layout = [[sg.Text('Adjetivos    '), sg.InputOptionMenu(cant['JJ'])],
            [sg.Text('Sustantivos'), sg.InputOptionMenu(cant['NN'])],
           [sg.Text('Verbos       '), sg.InputOptionMenu(cant['VB'])],
           [sg.Button('Enviar'), sg.Button('Volver')]]
    window = sg.Window('Cantidad de palabras a buscar', default_element_size=(40, 1), grab_anywhere=False).Layout(layout)
    event, values = window.Read()
