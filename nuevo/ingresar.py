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
          [sg.Button('Agregar'), sg.Button('Finalizar'),sg.Button('Eliminar')] ]

    #Muestro la ventana
    ventanaPalabras = sg.Window('Sopa de letras',auto_size_text=True,default_element_size=(40, 1)).Layout(diseñoPalabras)

    #Proceso la información
    tiposIngresados=('Adjetivos: ' + str(len(dicc['J'])) + '\n' + 'Sustantivos: ' + str(len(dicc['N'])) + '\n' + 'Verbos: ' + str(len(dicc['B']))) #Inicializo el mensaje a mostrar
    lista_palabras = []
    while True:     #Se ingresan palabras hasta que se haga clic en 'Finalizar'
        boton, datos = ventanaPalabras.Read()   #Leo los datos de la ventana
        palabra = datos[0].lower()
        if boton is None or boton == 'Finalizar':
            ventanaPalabras.Close()
            return (dicc)
        else:
            bool, tipo, defi = validaciones.validar(palabra) #Retorna tupla (bool,tipo,definicion)
            if bool:
                if boton == 'Agregar':
                    if palabra in lista_palabras:
                        mensaje='La palabra ya fue ingresada'
                    else:
                        dicc[tipo].append({ 'palabra': palabra, 'descripcion': ''.join(defi) })
                        mensaje = 'La palabra fue ingresada correctamente'
                        lista_palabras.append(palabra)
                        print(lista_palabras)
                if boton == 'Eliminar': 
                    if palabra in lista_palabras:
                        dicc[tipo] = list(filter(lambda di:di['palabra']!=palabra, dicc[tipo]))
                        lista_palabras.remove(palabra)
                        mensaje='La palabra se eliminó'
                    else:
                        mensaje='La palabra ingresada no está en la lista'
            else:
                sg.PopupError('La palabra ingresada no es valida')
            tiposIngresados=('Adjetivos: ' + str(len(dicc['J'])) + '\n' + 'Sustantivos: ' + str(len(dicc['N'])) + '\n' + 'Verbos: ' + str(len(dicc['B'])))
            ventanaPalabras.FindElement('mensaje').Update(mensaje)
            ventanaPalabras.FindElement('palabras').Update(tiposIngresados)


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