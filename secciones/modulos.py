import sys
import PySimpleGUI as sg
import random
import string

cant_celdas = 10 #Cantidad de celdas
tam_celda = 20 #Tamaño de cada celda
tam_grilla = cant_celdas*tam_celda + 200 #Tamaño de la grilla
grilla55 = (tam_grilla*55)/100
letters = string.ascii_lowercase

#Diseño de la ventana
layout = [
            [sg.Text('Sopa de letras'), sg.Text('', key='_OUTPUT_')],
            [sg.Graph((tam_grilla,tam_grilla), (0,grilla55), (grilla55,0), key='_GRAPH_', change_submits=True, drag_submits=False)],
            [sg.Button('Show'), sg.Button('Exit')]
         ]

window = sg.Window('Juego para niños', ).Layout(layout).Finalize()

g = window.FindElement('_GRAPH_')

for row in range(cant_celdas):
    for col in range(cant_celdas):
        g.DrawRectangle((col * tam_celda + 5, row * tam_celda + 3), (col * tam_celda + tam_celda + 5, row * tam_celda + tam_celda + 3), line_color='black')
        g.DrawText('{}'.format(random.choice(string.ascii_uppercase)), (col * tam_celda + 15, row * tam_celda + 12))

while True:             # Event Loop
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    mouse = values['_GRAPH_']

    if event == '_GRAPH_':
        if mouse == (None, None):   
            continue
        box_x = mouse[0]//tam_celda
        box_y = mouse[1]//tam_celda
        letter_location = (box_x * tam_celda + 18, box_y * tam_celda + 17)
        print('Coordenada elegida:')
        print(box_x, box_y)
        g.DrawRectangle((box_x * tam_celda + 5, box_y * tam_celda + 3), (box_x * tam_celda + tam_celda + 5, box_y * tam_celda + tam_celda + 3), line_color='black', fill_color='red')
        # g.DrawText('{}'.format(random.choice(string.ascii_uppercase)), letter_location, font='Courier 25')

window.Close()