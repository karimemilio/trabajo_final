"""Este modulo se encarga a medida que se va ingresando palabras procesar la informacion ingresando o no la palabra a la lista de la grilla,tambien
    va editando el mensaje que aparece cada vez q se va ingresando una palabra"""

from pattern.text.es import tag,parse, split
import PySimpleGUI as sg
from wiktionaryparser import WiktionaryParser
import validaciones

def generarPalabras(dicc):
    #Creo el diseño de la ventana
    diseñoPalabras = [[sg.Text('Ingrese una palabra')],
          [sg.Input(do_not_clear=False)],
          [sg.Text(' ', key= 'mensaje',size=(37,1))],
          [sg.Text(' ', key= 'palabras',size=(37,3))],
          [sg.Button('Agregar'), sg.Button('Siguiente'),sg.Button('Eliminar'),sg.Button('Lista de palabras')],
           [sg.Button('ver_reporte')] ]


    #Muestro la ventana
    ventanaPalabras = sg.Window('Sopa de letras',auto_size_text=True,default_element_size=(40, 1)).Layout(diseñoPalabras)

    #Proceso la información
    tiposIngresados=('Adjetivos: ' + str(len(dicc['J'])) + '\n' + 'Sustantivos: ' + str(len(dicc['N'])) + '\n' + 'Verbos: ' + str(len(dicc['B']))) #Inicializo el mensaje a mostrar
    lista_palabras = []
    reporte = []
    while True:     #Se ingresan palabras hasta que se haga clic en 'Siguiente'
        boton, datos = ventanaPalabras.Read()   #Leo los datos de la ventana
        if boton is None:
            ventanaPalabras.Close()
            return None
        elif boton == 'Siguiente':
            return (dicc)
        elif boton == 'ver_reporte':
            sg.PopupOK(reporte)
        elif boton == 'Lista de palabras':
            lis = []
            for pos in dicc:
                aux = str(pos)+':'
                for pal in dicc[pos]:
                    aux = aux + ' ' + str(pal['palabra']) + str(', ')
                lis.append(aux)
            sg.Popup('Palabras ingresadas', str(lis))
        else:
            palabra = datos[0].lower()
            if palabra == '':
                mensaje='No se especificó una palabra'
            else:
                bool, tipo, defi,reporte = validaciones.validar(palabra,reporte,boton) #Retorna tupla (bool,tipo,definicion)
                if bool:
                    if boton == 'Agregar':
                        if palabra in lista_palabras:
                            mensaje='La palabra ya fue ingresada'
                        else:
                            dicc[tipo].append({ 'palabra': palabra, 'descripcion': ''.join(defi) })
                            mensaje = 'La palabra fue ingresada correctamente'
                            lista_palabras.append(palabra)
                    if boton == 'Eliminar': 
                        if palabra in lista_palabras:
                            dicc[tipo] = list(filter(lambda di:di['palabra']!=palabra, dicc[tipo]))
                            lista_palabras.remove(palabra)
                            mensaje='La palabra se eliminó'
                    
                    else:   
                        mensaje='La palabra ingresada no está en la lista'
                else:
                    sg.PopupError('La palabra ingresada no es valida')
                tiposIngresados=('Adjetivos: ' + str(len(dicc['J'])) + '\n' + 'Sustantivos: ' + str(len(dicc['N'])) + '\n' + 'Verbos: ' + str(len(dicc['B'])))
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