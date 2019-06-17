from pattern.text.es import tag,parse, split
import PySimpleGUI as sg
from wiktionaryparser import WiktionaryParser
from secciones import validaciones

def generarPalabras(dicc):
    #Creo el diseño de la ventana
    diseñoPalabras = [[sg.Text('Ingrese una palabra')],      
          [sg.Input(do_not_clear=False)],
          [sg.Text(' ', key= 'mensaje',size=(37,1))],
          [sg.Text(' ', key= 'palabras',size=(37,3))],
          [sg.Button('Agregar'), sg.Button('Finalizar'),sg.Button('Eliminar')]]
    
    #Muestro la ventana
    ventanaPalabras = sg.Window('Sopa de letras',auto_size_text=True,default_element_size=(40, 1)).Layout(diseñoPalabras)      

    #Proceso la información
    tiposIngresados=('Adjetivos: ' + str(len(dicc['JJ'])) + '\n' + 'Sustantivos: ' + str(len(dicc['NN'])) + '\n' + 'Verbos: ' + str(len(dicc['VB']))) #Inicializo el mensaje a mostrar
    while True:     #Se ingresan palabras hasta que se haga clic en 'Finalizar'
        boton, datos = ventanaPalabras.Read()   #Leo los datos de la ventana
        palabra = datos[0]                #Obtengo la palabra ingresada
        if boton is None or boton == 'Finalizar':
            ventanaPalabras.Close()
            return dicc
        else:
            ingreso = validar(palabra) #Retorna tupla (bool,tipo,definicion)
        if ingreso[0]:
            if boton == 'Agregar':
                if palabra in dicc[ingreso[1]]:
                    mensaje='La palabra ya fue ingresada'
                else:
                    dicc[ingreso[1]].append((palabra,ingreso[2])) #Agrego al diccionario de listas una tupla (palabra,definicion)
                    mensaje='La palabra ingresada es válida'
            if boton == 'Eliminar': 
                if palabra in dicc[ingreso[1]]:
                    dicc[ingreso[1]].remove((palabra,ingreso[2]))
                    mensaje='La palabra se eliminó'
                else:
                    mensaje='La palabra ingresada no está en la lista'
        else:
            sg.PopupError('La palabra ingresada no es valida')
        tiposIngresados=('Adjetivos: ' + str(len(dicc['JJ'])) + '\n' + 'Sustantivos: ' + str(len(dicc['NN'])) + '\n' + 'Verbos: ' + str(len(dicc['VB'])))
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
