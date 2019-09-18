""" Modulos se encarga de verificar se cargaron minimamente 1 palabra de cada tipo (sustantivo,verbo,adjetivo) y se encarga de cargar la informacion"""
import ingresar as ip
import seleccion as sel
import PySimpleGUI as sg

def esVacio(dicc):
    if len(dicc['adjetivo']) > 0 and len(dicc['sustantivo']) > 0 and len(dicc['verbo']) > 0 :
        return False
    else:
        return True

def cargarInfo():

        #Inicializo el diccionario de palabras con las claves para cada tipo de palabra (adjetivo, sustantivo, verbo)
        dicc={'adjetivo': [] , 'sustantivo': [], 'verbo': []}

        #Armo el diseño de la ventana inicial
        diseñoInicial=[[sg.Text('  ¿Desea comenzar?', background_color='#b3d4fc',font=("scruff", 35))],
                [sg.Button('Si', button_color=('black','#AEA79F'),font=("scruff", 20)),
                sg.Button('No', button_color=('black','#AEA79F'),font=("scruff", 20))]]

        #Muestro la ventana
        ventanaInicial = sg.Window('Sopa de letras',auto_size_buttons=False,background_color='#b3d4fc').Layout(diseñoInicial)

        #Espero información y capturo eventos
        event, values = ventanaInicial.Read()
        resultado = None
        if event == 'Si':
            ventanaInicial.Close()
            dicc = ip.generarPalabras(dicc)
            if dicc == None or esVacio(dicc):
                return None,None
            else:
                resultado = sel.seleccion(dicc)
                if resultado == None:
                        return None,None
        else:
                ventanaInicial.Close()
        return (dicc,resultado)
