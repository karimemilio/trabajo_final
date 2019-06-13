import PySimpleGUI as sg
# palabra = 'Gato'
# text = sg.PopupGetText(palabra, 'Ingrese una definición')      
# sg.Popup('Resultados', 'La definición obtenida fue: ', text)      
dicc={'JJ': ['hola','chau'] , 'NN': ['chau','chau','chau'], 'VB': ['chau']}

cant = {}
for tipo in dicc:
    cant[tipo] = []
    for i in range(len(dicc[tipo])):
        cant[tipo].append(i+1)

#     lista = []
#     for i in range(len(dicc[tipo])):
#         lista.append(i)
#     tupla = (tuple(lista))
#     listaGral.append(tupla)
# tuplaGral = (tuple(listaGral))

layout = [[sg.Text('Adjetivos    '), sg.InputOptionMenu(cant['JJ'])],
            [sg.Text('Sustantivos'), sg.InputOptionMenu(cant['NN'])],
           [sg.Text('Verbos       '), sg.InputOptionMenu(cant['VB'])],
           [sg.Button('Enviar'), sg.Button('Volver')]]
window = sg.Window('Cantidad de palabras a buscar', default_element_size=(40, 1), grab_anywhere=False).Layout(layout)      
event, values = window.Read() 