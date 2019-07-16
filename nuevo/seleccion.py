import PySimpleGUI as sg
import random

colores = ['rojo', 'amarillo',  'verde', 'azul']
colors = ['red', 'yellow', 'green','blue'] 

def seleccion(dicc):
    cant = {}
    result = dicc.keys()
    claves = []
    lista = []
    for elem in result:
        agregado = []
        for i in range(len(dicc[elem])):
            agregado.append(i+1)
        lista.append(agregado)
    layout = [[sg.Text('Adjetivos    '),  sg.InputOptionMenu(lista[0]), sg.InputOptionMenu(colores)], 
    [sg.Text('Sustantivos'), sg.InputOptionMenu(lista[1]), sg.InputOptionMenu(colores)],
    [sg.Text('Verbos       '), sg.InputOptionMenu(lista[2]), sg.InputOptionMenu(colores)],
    [sg.Radio('Mayuscula', 'RADIO2', default=True), sg.Radio('Minuscula', 'RADIO2')],
    [sg.Radio('Horizontal', 'RADIO1', default = True ), sg.Radio('Vertical', 'RADIO1')],
    [sg.Checkbox('Ayuda')],
    [sg.Button('Enviar'), sg.Button('Volver')]]

    window = sg.Window('Cantidad de palabras a buscar', default_element_size=(40, 1), grab_anywhere=False).Layout(layout)
    event, values = window.Read()
    cant['J'] = { 'cantidad': int(values[0]), 'color': colors[colores.index(values[1])]}
    cant['N'] = { 'cantidad': int(values[2]), 'color': colors[colores.index(values[3])] }
    cant['B'] = { 'cantidad': int(values[4]), 'color': colors[colores.index(values[5])] }
    cant['mayuscula'] = True if values[6] else False
    cant['Horizontal'] = True if values[8] else False
    cant['ayuda'] = True if values[10] else False
    return cant