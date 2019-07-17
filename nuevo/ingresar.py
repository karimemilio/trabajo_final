#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import validaciones
import modulos

def agregarPredefinidas(dicc):
    if dicc['J'] == []:
        dicc['J'].append({ 'palabra': 'bonito', 'descripcion': 'Que tiene belleza o atractivo y resulta agradable de contemplar o de escuchar.'})
    if dicc['N'] == []:
        dicc['N'].append({ 'palabra': 'mesa', 'descripcion': 'Mueble formado por un tablero horizontal, sostenido por uno o varios pies, con la altura conveniente para poder realizar alguna actividad sobre ella o dejar cosas encima.'})
    if dicc['B'] == []:
        dicc['B'].append({ 'palabra': 'correr', 'descripcion': 'Desplazarse [una persona o un animal] rápidamente con pasos largos y de manera que levanta un pie del suelo antes de haber apoyado el otro.'})


def confirmar(msje):
    layout = [[sg.Text(msje)],[sg.Text('Está seguro que desea continuar?')],[sg.Button('Si'),sg.Button('Cancelar')]]
    confirm = sg.Window('Atención!').Layout(layout)
    press, data = confirm.Read()
    if press == 'Si':
        confirm.Close()
        return True
    else:
        confirm.Close()
        False
                
def mostrarPalabras(dicc):
    lis = []
    for pos in dicc:
        string = str(modulos.hashClaves(pos)) + ': '
        for pal in dicc[pos]:
            string = string + ' ' + str(pal['palabra']) + str(' - ')
        lis.append(string)
    sg.Popup('Palabras ingresadas', str(lis[0]), str(lis[1]), str(lis[2]))
    
def generarPalabras(dicc):
    """Muestra la ventana de ingreso de palabras. Permite ingresar una palabra para agregar o eliminarla.
    Éste módulo invoca a la validación de dichas palabras para saber si debe agregarlas/eliminarlas del diccionario"""
    #Creo el diseño de la ventana de ingreso de palabras
    diseñoPalabras = [[sg.Text('Ingrese una palabra')],
          [sg.Input(do_not_clear=False)],
          [sg.Text(' ', key= 'mensaje',size=(37,1))],
          [sg.Text(' ', key= 'palabras',size=(37,3))],
          [sg.Button('Agregar palabra'),sg.Button('Eliminar palabra')],
          [sg.Button('Avanzar'),sg.Button('Lista de palabras'),sg.Button('Salir del juego')]]

    #Muestro la ventana de ingreso de palabras (carga)
    ventanaPalabras = sg.Window('Sopa de letras',auto_size_text=True,default_element_size=(40, 1)).Layout(diseñoPalabras)

    #Proceso la información
    tiposIngresados=('Adjetivos: ' + str(len(dicc['J'])) + '\n' + 'Sustantivos: ' + str(len(dicc['N'])) + '\n' + 'Verbos: ' + str(len(dicc['B']))) #Inicializo el mensaje a mostrar
    lista_palabras = []
    reporte = []
    while True:     #Se ingresan palabras hasta que se haga clic en 'Finalizar'
        boton, datos = ventanaPalabras.Read()   #Leo los datos de la ventana
        if boton is None:
            ventanaPalabras.Close()
            return None
        if boton == 'Salir del juego':
            msje = 'Usted está a punto de salir del juego'
            if confirmar(msje):
                ventanaPalabras.Close()
                return None
        elif boton == 'Avanzar':
            if modulos.esVacio(dicc):
                msje = 'No se ingresaron palabras suficientes.\nDeberá ingresar al menos una por cada tipo de palabra\nSi continúa se completará el diccionario de palabras con predefinidas'
            else:
                msje = 'Las palabras fueron almacenadas correctamente'
            if confirmar(msje):
                agregarPredefinidas(dicc)
                ventanaPalabras.Close()
                return (dicc)
        elif boton == 'Lista de palabras':
            mostrarPalabras(dicc)
        else:
            palabra = datos[0].lower()
            if palabra == '':
                sg.Popup('Atención!', 'Pasos a seguir para agregar o eliminar una palabra:','1) Escribirla en el campo superior', '2) Seleccionar la acción a realizar (agregar o eliminar)')
                mensaje='Ingrese una palabra en el espacio de arriba'
            else:
                bool, tipo, defi = validaciones.validar(palabra,reporte,boton) #Retorna tupla (bool,tipo,definicion)
                if bool:
                    if boton == 'Agregar palabra':
                        if palabra in lista_palabras:
                            mensaje='La palabra ya fue ingresada'
                        else:
                            dicc[tipo].append({ 'palabra': palabra, 'descripcion': ''.join(defi) })
                            mensaje = 'La palabra fue ingresada correctamente'
                            lista_palabras.append(palabra)
                    if boton == 'Eliminar palabra': 
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