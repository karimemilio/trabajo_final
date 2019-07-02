import PySimpleGUI as sg
import random

colores = ['rojo', 'amarillo', 'blanco', 'negro', 'verde']
colors = ['red', 'yellow', 'white', 'black', 'green'] 

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
    cant['Horinzontal'] = True if values[8] else False
    cant['ayuda'] = True if values[10] else False
    #Cree diccionario con clave:valor --> tipo de palabra:cantidad a elegir --> JJ:2
    #nue = {}
    #for tipo in cant:
    #    nue[tipo] = []  #Diccionario del tipo clave:valor --> tipo de palabra : lista de palabaras seleccionadas
    #    for i in range(cant[tipo]):
    #        aux=random.choice(dicc[tipo])
    #        while aux in nue[tipo]:
    #            aux=random.choice(dicc[tipo])
    #        nue[tipo].append(aux)

    return cant