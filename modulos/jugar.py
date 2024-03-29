import PySimpleGUI as sg
import string
import random
import copy
import sys

""" EL modulo jugar  crea la grilla de la sopa de letras, y a partir de la configuracion que se le pasa por parametros ,configura  la grilla con dichos parametros
    Tambien es el encargado de ir tomando una accion a medida que el usuario va clickiando cada una de las letras."""

#Convierte el las coordenadas y , x en una string 'y,x'
def hash (y,x):
    pos = (str(y)+','+str(x))
    return pos

#Cheackea que todas las letras de la palabra esten seleccionadas
def check(aux):
    for elem in aux:
        if elem['selc'] == False:
            return False
    return True

#Actualiza los datos seleccionados en la grilla
def actualizar_datos(final,y,x,color,estado_Actual):
    condicion = False
    for each in final:
        for elem in each['posiciones']:
            if elem['pos'] == (y,x):
                estado_Actual[hash(y,x)]['esPalabra'] = True
                if 'pintura' in elem.keys():
                    if elem['pintura'] == color:
                        elem['pintura'] = 'white'
                        elem['selc']= False
                    else:
                        elem['pintura'] = color
                        elem['selc'] = True
                else: 
                    elem['pintura'] = color
                    elem['selc'] =True
                condicion = (True if elem['selc'] else False) 
                if check(each['posiciones']):
                    each['si'] = True
                else:
                    each['si'] = False
                break   
    return final,condicion

def jugar(palabras, config):
    ####################CAMBIOS################
    cant_celdas = getLongitudMaxima(palabras) + 5 #Cantidad de celdas
    if cant_celdas < 15: 
        tam_celda = 20 
    else:
        tam_celda = 15 #Tamaño de cada celda
    tam_grilla = cant_celdas*tam_celda +300
    grilla55 = (tam_grilla*55)/100
    mayus = string.ascii_lowercase
    minus = string.ascii_uppercase

    solucion = [[sg.Graph((tam_grilla,tam_grilla), (0,grilla55), (grilla55,0), key='_SOL_', change_submits=True, drag_submits=False)]]

    if config['ayuda'] == True:
        #Diseño de la ventana con ayuda
        layout = [
                    [sg.Text('Sopa de letras'), sg.Text('', key='_OUTPUT_')],
                    [sg.Button('--Ayuda--',button_color = ('white','black'),key= 'A')],
                    [sg.Graph((tam_grilla,tam_grilla), (0,grilla55), (grilla55,0), key='_GRAPH_', change_submits=True, drag_submits=False)],
                    [sg.Button('Verbo', button_color=('black',config['verbo']['color'])),sg.Button('Adjetivo', button_color=('black',config['adjetivo']['color'])),sg.Button('Sustantivo', button_color=('black',config['sustantivo']['color'])), sg.Button('Finalizar',key = 'fin'), sg.Button('Exit')]
                ]
    else:
        #Diseño de la ventana sin ayuda
        layout = [
                    [sg.Text('Sopa de letras'), sg.Text('', key='_OUTPUT_')],
                    [sg.Graph((tam_grilla,tam_grilla), (0,grilla55), (grilla55,0), key='_GRAPH_', change_submits=True, drag_submits=False)],
                    [sg.Button('Verbo', button_color=('black',config['verbo']['color'])),sg.Button('Adjetivo', button_color=('black',config['adjetivo']['color'])),sg.Button('Sustantivo', button_color=('black',config['sustantivo']['color'])), sg.Button('Finalizar',key = 'fin'), sg.Button('Exit')]
                ]

    #Crear estructura
    filas = []

    for i in range(0, cant_celdas):
        columna = []
        for i in range(0, cant_celdas):
            columna.append('')
        filas.append(columna)

    final_guardadas = []
    
    #Compara si las letras seleccionadas corresponden a todas las palabras,a su clasificacion y que no haya apretado otras letras de mas
    def comparar(final_guardadas,estado_Actual):
        for each in final_guardadas:
            if not each['si']:
                sg.Popup('No se marcaron todas las palabras')
                return False                                    #False si faltan palabras
            color = config[each['tipo']]['color']
            for elem in each['posiciones']:
                if elem['pintura'] != color:
                    sg.Popup('Las palabras no se marcaron con el color correcto')
                    return  False                               #False si su clasificacion es incorrecta
        for i in estado_Actual: 
            if (estado_Actual[i]['apretado'] == True) and (estado_Actual[i]['esPalabra'] == False):
                sg.Popup('Se seleccionaron casilleros de mas')
                return False                                    #False si hay letras de mas seleccionadas
        return True         
    buscar = []
    #Arma de manera vertical la sopa
    def armado_Vertical(lista_de_palabras):         
        for palabra,tipo in lista_de_palabras:
            buscar.append(palabra)
            no_termino = True
            while no_termino:
                fila = random.randint(0, cant_celdas - len(palabra))
                columna = random.randint(0, cant_celdas )
                se_puede = True
                try:
                    for i in range(fila, len(palabra)):
                        if filas[i][columna] != '':
                            se_puede = False
                            break
                    if se_puede:
                        aux = columna
                        diccionario = { 'palabra': palabra,'posiciones': [], 'si':False, 'tipo':tipo}
                        for elemento in palabra:
                            if config["mayuscula"] == True:
                                elemento = elemento.upper()
                            dic_posiciones = {}
                            dic_posiciones['pos'] = (fila,aux)
                            dic_posiciones['selc'] = False
                            dic_posiciones['pintura'] = 'white'
                            diccionario['posiciones'].append(dic_posiciones)
                            filas[fila][aux] = elemento
                            fila +=1
                        final_guardadas.append(diccionario)
                        no_termino = False
                except (IndexError):
                    pass

    #Arma de manera horizontal la sopa
    def armado_Horizontal(lista_de_palabras):       
        for palabra,tipo in lista_de_palabras:
            buscar.append(palabra)  
            no_termino = True
            while no_termino:
                fila = random.randint(0, cant_celdas)
                columna = random.randint(0, cant_celdas - len(palabra))
                se_puede = True
                try:
                    for i in range(columna, len(palabra)):
                        if filas[fila-1][i] != '': 
                            se_puede = False
                            break
                    if se_puede:
                        diccionario = { 'palabra': palabra,'posiciones': [], 'si':False, 'tipo':tipo}
                        for elemento in palabra:
                            if config["mayuscula"] == True:
                                elemento = elemento.upper()
                            dic_posiciones = {}
                            dic_posiciones['pos'] = (fila,columna)
                            dic_posiciones['selc'] = False
                            diccionario['posiciones'].append(dic_posiciones)
                            filas[fila][columna] = elemento
                            columna += 1
                        final_guardadas.append(diccionario)
                        no_termino = False
                except (IndexError):
                        pass


    lista_de_palabras = getAllPalabras(palabras)

    if config['Horizontal']:
        armado_Horizontal(lista_de_palabras)
    else:
        armado_Vertical(lista_de_palabras)
    
    aux_filas = copy.deepcopy(filas)

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

    def ayuda():
        descri = []
        for elem in palabras:
            for lista in palabras[elem]:
                descri.append(lista['descripcion'])
        sg.PopupOK(descri)
        
    #Crea la lista de estados_Actualues de las difenrentes letras de la sopa
    estado_Actual = {}
    for i in range(0,len(filas)):
        for j in  range(0,len(filas[0])):
            coor = hash(j,i)
            estado_Actual[coor] = {'apretado' : False, 'color' : 'white', 'esPalabra' : False} 

    #Crear la vista
    window = sg.Window('Juego para niños', resizable=True).Layout(layout).Finalize()

    g = window.FindElement('_GRAPH_')
    #Crea la matriz
    for row in range(cant_celdas):
        for col in range(cant_celdas):
            g.DrawRectangle((col * tam_celda + 5, row * tam_celda + 3), (col * tam_celda + tam_celda + 5, row * tam_celda + tam_celda + 3), fill_color = 'white',line_color='black')
            g.DrawText('{}'.format(filas[row][col]), (col * tam_celda + 15, row * tam_celda + 12))
    while True:             # Event Loop        
        event, values = window.Read()
        if event is None or 'tipo' == 'Exit':
            break
        if event == 'Sustantivo':
                color = config['sustantivo']['color']
        elif event == 'Adjetivo':
                color = config['adjetivo']['color']
        elif event == 'Verbo':
            color=config['verbo']['color']
        elif event == 'A':
            ayuda()
        elif event == 'fin':
            if comparar(final_guardadas,estado_Actual):
                sg.Popup('La respuesta es correcta')
            else:
                sg.Popup('La respuesta es incorrecta')
        elif event == 'Exit':
            if not comparar(final_guardadas,estado_Actual):
                sg.Popup('Las palabras a adivinar eran: ', buscar)
                #Crear la vista
                ventana = sg.Window('Solución', resizable=True).Layout(solucion).Finalize()
                sol_aux = ventana.FindElement('_SOL_')
                 #Crea la matriz
                for x1 in range(cant_celdas):
                    for y1 in range(cant_celdas):
                        sol_aux.DrawRectangle((y1 * tam_celda + 5, x1 * tam_celda + 3), (y1 * tam_celda + tam_celda + 5, x1 * tam_celda + tam_celda + 3), fill_color = 'white',line_color='black')
                        sol_aux.DrawText('{}'.format(aux_filas[x1][y1]), (y1 * tam_celda + 15, x1 * tam_celda + 12))
                while True:
                    evento, valor = ventana.Read()
                    if evento != None:
                        break
            sg.Popup('FIN DEL JUEGO')
            break
        mouse = values['_GRAPH_']
        if event == '_GRAPH_':
            if mouse == (None, None):
                continue
            box_x = mouse[0]//tam_celda
            box_y = mouse[1]//tam_celda
            letter_location = (box_y,box_x)
            try:
                final_guardadas,condicion = actualizar_datos(final_guardadas, box_y,box_x,color,estado_Actual)
                actual = filas[box_y][box_x]     
                coord = hash(box_y, box_x)
                if estado_Actual[coord]['color'] == color:
                    estado_Actual[coord]['color'] = 'white'
                    estado_Actual[coord]['apretado'] = False
                else:
                    estado_Actual[coord]['color'] = color
                    estado_Actual[coord]['apretado'] = True
                g.DrawRectangle((box_x * tam_celda + 5, box_y * tam_celda + 3), (box_x * tam_celda + tam_celda + 5, box_y * tam_celda + tam_celda + 3), line_color='black', fill_color = estado_Actual[coord]['color'])
                g.DrawText(actual,(box_x * tam_celda + 15, box_y * tam_celda + 12))
            except (UnboundLocalError):
                sg.Popup('Elegir color')
            except (IndexError):
                sg.Popup('Seleccion fuera de la grilla')

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
    for each in palabras:
        for elemento in palabras[each]:
            lista.append((elemento['palabra'],each))
    return lista