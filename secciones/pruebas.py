import PySimpleGUI as sg
import random
import string
import sys

letters = string.ascii_lowercase

celdas = 10
BOX_SIZE = 20
tam = 500
    
layout = [      
        [sg.Graph(canvas_size=(tam, tam), graph_bottom_left=(0,200), graph_top_right=(200, 0), background_color='grey', key='graph',  change_submits=True, drag_submits=False)],    
        [sg.T('Palabra a elegir:'), sg.Button('Verbo', button_color=('black', 'green')), sg.Button('Adjetivo', button_color=('black', 'yellow')), sg.Button('Sustantivo', button_color=('black', 'red'))]      
        ]      
    
window = sg.Window('Sopa de letras', layout)      
window.Finalize()

g = window.Element('graph')

for row in range(celdas):
    for col in range(celdas):
        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        g.DrawText('{}'.format(random.choice(letters)), (col * BOX_SIZE + 10, row * BOX_SIZE + 8))

# circle = graph.DrawCircle((75,75), 25, fill_color='black',line_color='white')      
# point = graph.DrawPoint((75,75), 10, color='green')      
# oval = graph.DrawOval((25,300), (100,280), fill_color='purple', line_color='purple'  )      
# rectangle = graph.DrawRectangle((25,300), (100,280), line_color='purple'  )      
# line = graph.DrawLine((0,0), (100,100))      
    
while True:      
    event, values = window.Read()      
    if event is None:      
        break      
    if event is 'Verbo':      
        graph.TKCanvas.itemconfig(circle, fill = "Blue")      
    elif event is 'Adjetivo':      
        graph.TKCanvas.itemconfig(circle, fill = "Red")      
    elif event is 'Sustantivo':      
        graph.MoveFigure(point, 10,10)      
        graph.MoveFigure(circle, 10,10)      
        graph.MoveFigure(oval, 10,10)      
        graph.MoveFigure(rectangle, 10,10)   