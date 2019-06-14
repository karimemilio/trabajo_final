from secciones import ingresar as ip
from secciones import seleccion as sel
import PySimpleGUI as sg

def esVacio(dicc):
    if len(dicc['JJ']) > 0 or len(dicc['NN']) > 0 or len(dicc['VB']) > 0 :
        return False
    else:
        return True

def cargarInfo():
        dicc={'JJ': [] , 'NN': [], 'VB': []}    #Creo un diccionario vacío

        #Creo el diseño de la ventana
        diseñoInicial=[[sg.Text('  ¿Desea comenzar?', background_color='#e96b27',font=("scruff", 35))],
                [sg.Button('Si', button_color=('black','#e96b27'),font=("scruff", 20)),
                sg.Button('No', button_color=('black','#e96b27'),font=("scruff", 20))]]
        
        #Muestro la ventana
        ventanaInicial = sg.Window('Sopa de letras',auto_size_buttons=False,background_color='#e96b27').Layout(diseñoInicial) 
        
        #Espero información
        event, values = ventanaInicial.Read()
        if event == 'Si':
            dicc = ip.generarPalabras(dicc)
        else: 
            print('No quiso jugar :(')
        ventanaInicial.Close()
        if esVacio(dicc): 
            return None
        else:
            return sel.seleccion(dicc)

def jugar(dicc):
    return None