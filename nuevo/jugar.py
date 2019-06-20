import PySimpleGUI as sg
import string
import random
import sys

def jugar(palabras, config):
    cant_celdas = getLongitudMaxima(palabras) + 4 #Cantidad de celdas
    tam_celda = 20 #Tamaño de cada celda
    tam_grilla = cant_celdas*tam_celda +200
    grilla55 = (tam_grilla*55)/100
    letters = string.ascii_lowercase

    #Diseño de la ventana
    layout = [
                [sg.Text('Sopa de letras'), sg.Text('', key='_OUTPUT_')],
                [sg.Graph((tam_grilla,tam_grilla), (0,grilla55), (grilla55,0), key='_GRAPH_', change_submits=True, drag_submits=False)],
                [sg.Button('Show'), sg.Button('Exit')]
             ]

    #Crear estructura
    filas = []

    for i in range(0, cant_celdas):
        columna = []
        for i in range(0, cant_celdas):
            columna.append('')
        filas.append(columna)

    final_guardadas = []

    #Insertar todas las palabras
    lista_de_palabras = getAllPalabras(palabras)
    for palabra in lista_de_palabras:
        no_termino = True
        while no_termino:
            fila = random.randint(0, cant_celdas)
            columna = random.randint(0, cant_celdas - len(palabra))
            se_puede = True
            for i in range(columna, len(palabra)):
                if filas[fila-1][i] != '':
                    se_puede = False
                    break
            if se_puede:
                aux = columna
                for elemento in palabra:
                    filas[fila-1][aux] = elemento
                    aux += 1
                final_guardadas.append({ 'palabra': palabra, 'columna': (fila, columna) })
                no_termino = False

    #Insertar letras en el resto de la matriz
    nro_columna = 0
    for columna in filas:
        nro_caracter = 0
        for posicion in columna:
            if posicion == '':
                caracter = random.choice(string.ascii_uppercase if config['mayuscula'] else string.ascii_lowercase)
                filas[nro_columna][nro_caracter] = caracter
            nro_caracter += 1
        nro_columna += 1

    print(filas)
    print('-------------')
    print(final_guardadas)

    #Crear la vista
    window = sg.Window('Juego para niños', ).Layout(layout).Finalize()

    g = window.FindElement('_GRAPH_')

    for row in range(cant_celdas):
        for col in range(cant_celdas):
            g.DrawRectangle((col * tam_celda + 5, row * tam_celda + 3), (col * tam_celda + tam_celda + 5, row * tam_celda + tam_celda + 3), line_color='black')
            g.DrawText('{}'.format(filas[row][col]), (col * tam_celda + 15, row * tam_celda + 12))

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
            letter_location = (box_y, box_x )
            print('Coordenada elegida:')
            print(box_y + 1, box_x)
            g.DrawRectangle((box_x * tam_celda + 5, box_y * tam_celda + 3), (box_x * tam_celda + tam_celda + 5, box_y * tam_celda + tam_celda + 3), line_color='black', fill_color='red')
            # g.DrawText('{}'.format(random.choice(string.ascii_uppercase)), letter_location, font='Courier 25')

def getLongitudMaxima(palabras):
    longitud = 0
    for elemento in palabras.values():
        for diccionario in elemento:
            if len(diccionario['palabra']) > longitud:
                longitud = len(diccionario['palabra'])

    return longitud

def getAllPalabras(palabras):
    lista = []
    for elemento in palabras.values():
        for diccionario in elemento:
            lista.append(diccionario['palabra'])

    return lista
