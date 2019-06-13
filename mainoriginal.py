import json
from pattern.text.es import tag,parse, split
import PySimpleGUI as sg
from wiktionaryparser import WiktionaryParser

from pattern.web import Wiktionary

def validacion(dat):
    parser = WiktionaryParser()
    parser.set_default_language('spanish')
    word = (parser.fetch(dat))[0]
    data = word['etymology']
    if (len(data) > 1):
        return True
    else:
        return False

def generarPalabras():
    #Creo el diseño de la ventana
    diseñoPalabras = [[sg.Text('Ingrese una palabra')],      
          [sg.Input(do_not_clear=False)],
          [sg.Text(' ', key= 'mensaje',size=(37,1))],
          [sg.Text(' ', key= 'palabras',size=(37,3))],
          [sg.Button('Validar palabra'), sg.Button('Finalizar')]]
    
    #Muestro la ventana
    ventanaPalabras = sg.Window('Sopa de letras',auto_size_text=True,default_element_size=(40, 1)).Layout(diseñoPalabras)      

    #Proceso la información
    ret = None  #Establezco un valor de retorno nulo
    dicc={'JJ': [] , 'NN': [], 'VB': []}    #Creo un diccionario vacío
    tiposIngresados=('Adjetivos: ' + str(len(dicc['JJ'])) + '\n' + 'Sustantivos: ' + str(len(dicc['NN'])) + '\n' + 'Verbos: ' + str(len(dicc['VB']))) #Inicializo el mensaje a mostrar
    while True:     #Se ingresan palabras hasta que se haga clic en 'Finalizar'
        boton, datos = ventanaPalabras.Read()   #Leo los datos de la ventana
        palabra = datos[0]                #Obtengo la palabra ingresada
        if boton is None or boton == 'Finalizar':
            ventanaPalabras.Close()
            return ret
        else:
            if validacion(palabra):
                tipo = (tag(palabra))[0][1]    #tag('palabra') devuelve una lista con una tupla (palabra,clasificacion)
                if palabra in dicc[tipo]:
                    mensaje='La palabra ya fue ingresada'
                else:
                    dicc[tipo].append(palabra)
                    tiposIngresados=('Adjetivos: ' + str(len(dicc['JJ'])) + '\n' + 'Sustantivos: ' + str(len(dicc['NN'])) + '\n' + 'Verbos: ' + str(len(dicc['VB'])))
                    mensaje='La palabra ingresada es válida'
                    ret = dicc
            else:
                mensaje='No se pudo clasificar la palabra'
            ventanaPalabras.FindElement('mensaje').Update(mensaje)
            ventanaPalabras.FindElement('palabras').Update(tiposIngresados)
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

def main():
    #Creo el diseño de la ventana
    diseñoInicial=[[sg.Text('  ¿Desea comenzar?', background_color='#e96b27',font=("scruff", 35))],
             [sg.Button('Si', button_color=('black','#e96b27'),font=("scruff", 20)),
             sg.Button('No', button_color=('black','#e96b27'),font=("scruff", 20))]]
    
    #Muestro la ventana
    ventanaInicial = sg.Window('Sopa de letras',auto_size_buttons=False,background_color='#e96b27').Layout(diseñoInicial) 
    
    #Espero información
    ok = False
    while True:
        event, values = ventanaInicial.Read()
        if event is None or event == 'No':
            break
        else:
            dicc = generarPalabras()
            if dicc != None:
                ok = True
                break
            else:
                print('No se registraron palabras :(')
    ventanaInicial.Close()
    if ok:
        seleccion(dicc)
    else:
        print('No quiso jugar :(')

if __name__=='__main__':	#Esta condicion se cumple si el módulo no es importado
    main()

# if event is 'Blue':
#         graph.TKCanvas.itemconfig(circle, fill="Blue")