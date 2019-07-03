import PySimpleGUI as sg
import string
import random
import sys
def hash (y,x):
    pos = (str(y)+','+str(x))
    return pos

def actualizar_datos(final,indice,y,x):
    y = y + 1
    print("---Entra al actualizar----")
    posi = hash(y,x)
    palabra = indice[posi]
    fi = final[palabra]
    print(fi)
    for each in final[palabra]:
        print("entra al for")
        if(each['pos'] == (y,x)):
            each['selec'] = not each['selec']
            break
    print("Sale del actualizar---")
    return final


    # i_final = 0
    # print (final)
    # print(" ")
    # for pos in final:
    #     for posicion in pos['posiciones']:
    #         if posicion['pos'] == (y,x):
    #             final[i_final]['selec'] = True
    #             cumple = True
    #             for elem in pos['posiciones']:
    #                 if not elem['selec']:
    #                     cumple = False
    #             if cumple:
    #                 final[i_final]['si'] = True
    #             break
    #     i_final += 1
    # print(final)
    # return final



def jugar(palabras, config):
    cant_celdas = getLongitudMaxima(palabras) + 4 #Cantidad de celdas
    tam_celda = 20 #Tamaño de cada celda
    tam_grilla = cant_celdas*tam_celda +200
    grilla55 = (tam_grilla*55)/100
    mayus = string.ascii_lowercase
    minus = string.ascii_uppercase

    #Diseño de la ventana
    layout = [
                [sg.Text('Sopa de letras'), sg.Text('', key='_OUTPUT_')],
                [sg.Graph((tam_grilla,tam_grilla), (0,grilla55), (grilla55,0), key='_GRAPH_', change_submits=True, drag_submits=False)],
                [sg.Button('Verbo', button_color=('black',config['B']['color'])),sg.Button('Adjetivo', button_color=('black',config['J']['color'])),sg.Button('Sustantivo', button_color=('black',config['N']['color']))],
                [sg.Button('Finalizar',key = 'tipo'), sg.Button('Exit')]
             ]

    #Crear estructura
    filas = []

    for i in range(0, cant_celdas):
        columna = []
        for i in range(0, cant_celdas):
            columna.append('')
        filas.append(columna)

    final_guardadas = []
    indice_palabras = {}

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
                diccionario = { 'palabra': palabra,'posiciones': [], 'si':False}
                for elemento in palabra:
                    if config["mayuscula"] == True:
                        elemento = elemento.upper()
                    dic_posiciones = {}
                    dic_posiciones['pos'] = (fila,aux)
                    indice_palabras[hash(fila,aux)] = palabra
                    dic_posiciones['selc'] = False
                    diccionario['posiciones'].append(dic_posiciones)
                    filas[fila-1][aux] = elemento
                    aux += 1
                final_guardadas.append(diccionario)
                no_termino = False


    #Insertar letras en el resto de la matriz
    nro_columna = 0
    for columna in filas:
        nro_caracter = 0
        for posicion in columna:
            if posicion == '':
                if config["mayuscula"]:
                    caracter = random.choice(minus)
                else:
                    caracter = random.choice(mayus)
                filas[nro_columna][nro_caracter] = caracter
            nro_caracter += 1
        nro_columna += 1

    print(filas)
    print('-------------')
    print(final_guardadas)


    #Crear la vista
    window = sg.Window('Juego para niños', ).Layout(layout).Finalize()

    g = window.FindElement('_GRAPH_')
    #Crea la matriz
    for row in range(cant_celdas):
        for col in range(cant_celdas):
            g.DrawRectangle((col * tam_celda + 5, row * tam_celda + 3), (col * tam_celda + tam_celda + 5, row * tam_celda + tam_celda + 3), line_color='black')
            g.DrawText('{}'.format(filas[row][col]), (col * tam_celda + 15, row * tam_celda + 12))

    while True:             # Event Loop
        try:
            event, values = window.Read()
            if event is None or 'tipo' == 'Exit':
                break
            if event == 'Sustantivo':
                    color = config['N']['color']
            elif event == 'Adjetivo':
                    color = config['J']['color']
            elif event == 'Verbo':
                color=config['B']['color']
            mouse = values['_GRAPH_']
            if event == '_GRAPH_':
                if mouse == (None, None):
                    continue
                box_x = mouse[0]//tam_celda
                box_y = mouse[1]//tam_celda
                letter_location = (box_y + 1,box_x)
                print('Coordenada elegida:')
                print (letter_location)
                final_guardadas = actualizar_datos(final_guardadas,indice_palabras, box_y,box_x)
                print ("-----------------y aca ----------")
                print (final_guardadas)


                # g.DrawRectangle((box_x * tam_celda + 5, box_y * tam_celda + 3), (box_x * tam_celda + tam_celda + 5, box_y * tam_celda + tam_celda + 3), line_color='black', fill_color= color)
                # filas[box_y][box_x] = actual
                # g.DrawText(actual,(box_x * tam_celda + 15, box_y * tam_celda + 12))

                actual = filas[box_y][box_x]  
                print(actual)
                g.DrawRectangle ( ((box_x * tam_celda + 5, box_y) * tam_celda + 3), (box_x * tam_celda + tam_celda + 5, box_y * tam_celda + tam_celda + 3), line_color='yellow',fill_color = color) 
                g.DrawText(actual, (box_x * tam_celda + 15, box_y * tam_celda + 12))
        except:
            pass
#Funcion que recupera la longitud maxima de la palabra mas larga
def getLongitudMaxima(palabras):
    longitud = 0
    for elemento in palabras.values():
        for diccionario in elemento:
            if len(diccionario['palabra']) > longitud:
                longitud = len(diccionario['palabra'])

    return longitud
#Funcion que recupera una lista con todas las palbras ingresadas
def getAllPalabras(palabras):
    lista = []
    for elemento in palabras.values():
        for diccionario in elemento:
            lista.append(diccionario['palabra'])

    return lista
