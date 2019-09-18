"""Seleccion se encarga de la parte visual de la configuracion que hace el usuario para la sopa de letra """
import PySimpleGUI as sg
import random

colores = ['rojo', 'amarillo',  'verde', 'azul']
colors = ['red', 'yellow', 'green','blue'] 

def seleccion(dicc):
    cant = {}
    result = dicc.keys()
    lista = []
    for elem in result:
        agregado = []
        for i in range(len(dicc[elem])):
            agregado.append(i+1)
        lista.append(agregado)
    layout = [[sg.Text('Adjetivos    ',background_color='#b3d4fc'),  sg.InputOptionMenu(lista[0],background_color='#AEA79F'), sg.InputOptionMenu(colores,default_value=colores[0],background_color='#AEA79F')], 
    [sg.Text('Sustantivos',background_color='#b3d4fc'), sg.InputOptionMenu(lista[1],background_color='#AEA79F'), sg.InputOptionMenu(colores,default_value=colores[1],background_color='#AEA79F')],
    [sg.Text('Verbos       ',background_color='#b3d4fc'), sg.InputOptionMenu(lista[2],background_color='#AEA79F'), sg.InputOptionMenu(colores,default_value=colores[2],background_color='#AEA79F')],
    [sg.Radio('Mayuscula', 'RADIO2', default=True,background_color='#b3d4fc'), sg.Radio('Minuscula', 'RADIO2',background_color='#b3d4fc')],
    [sg.Radio('Horizontal', 'RADIO1', default = True ,background_color='#b3d4fc'), sg.Radio('Vertical', 'RADIO1',background_color='#b3d4fc')],
    [sg.Checkbox('Ayuda',background_color='#b3d4fc')],
    [sg.Button('Enviar', button_color=('black','#AEA79F')), sg.Button('Salir', button_color=('black','#AEA79F')), sg.Button('?', button_color=("White", "Red"))]]

    window = sg.Window('Cantidad de palabras a buscar', default_element_size=(200, 200), grab_anywhere=False,background_color='#b3d4fc').Layout(layout)
    while True:
        event, values = window.Read()
        cant['adjetivo'] = { 'cantidad': int(values[0]), 'color': colors[colores.index(values[1])]}
        cant['sustantivo'] = { 'cantidad': int(values[2]), 'color': colors[colores.index(values[3])] }
        cant['verbo'] = { 'cantidad': int(values[4]), 'color': colors[colores.index(values[5])] }
        cant['mayuscula'] = True if values[6] else False
        cant['Horizontal'] = True if values[8] else False
        cant['ayuda'] = True if values[10] else False
        if event == 'Salir':
            return None
        if event == '?':
            sg.Popup('Configuración de la sopa:\n\n>Por cada tipo de palabra debe seleccionar la cantidad de palabras a usar y el color que se le asociará durante el juego\n>También podrá configurar la sopa de letras para que sea en minúscula o en mayúscula\n>Podrá configurar el sentido en el que aparecerán las palabras (Horizontal o vertical)\n>Puede configurar una ayuda opcional tildando la casilla "Ayuda"', title='Configuración',background_color='#b3d4fc',button_color=('black','#AEA79F'))    
        if event == 'Enviar':
            if (cant['verbo']['color'] != cant['sustantivo']['color']) and (cant['verbo']['color'] != cant['adjetivo']['color']) and (cant['sustantivo']['color'] != cant['adjetivo']['color']):
                break
            else:
                sg.Popup('Seleccionar colores distintos!!', button_type='POPUP_BUTTONS_ERROR', auto_close=True,auto_close_duration=4,icon='DEFAULT_WINDOW_ICON',background_color='#b3d4fc', button_color=('black','#AEA79F'))
    window.Close()
    return cant