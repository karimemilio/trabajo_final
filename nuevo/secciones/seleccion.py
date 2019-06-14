import PySimpleGUI as sg
import random

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
    cant['JJ'] = int(values[0])
    cant['NN'] = int(values[1])
    cant['VB'] = int(values[2])
    #Cree diccionario con clave:valor --> tipo de palabra:cantidad a elegir --> JJ:2
    nue = {}
    for tipo in cant:
        nue[tipo] = []  #Diccionario del tipo clave:valor --> tipo de palabra : lista de palabaras seleccionadas
        for i in range(cant[tipo]):
            aux=random.choice(dicc[tipo])
            while aux in nue[tipo]:
                aux=random.choice(dicc[tipo])
            nue[tipo].append(aux)
    return nue