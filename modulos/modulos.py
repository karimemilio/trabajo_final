""" Modulos se encarga de verificar se cargaron minimamente 1 palabra de cada tipo (sustantivo,verbo,adjetivo) y se encarga de cargar la informacion"""
import ingresar as ip
import seleccion as sel
import jugar as jugar_modulo
import PySimpleGUI as sg

def hashClaves(aux):
        if aux == 'J':
                return 'Adjetivos'
        elif aux == 'N':
                return 'Sustantivos'
        elif aux == 'B':
                return 'Verbos'
        else:
                print('Hubo un error en el hashing de claves')
                return None

def esVacio(dicc):
    if len(dicc['J']) > 0 or len(dicc['N']) > 0 or len(dicc['B']) > 0 :
        return False
    else:
        return True

def cargarInfo():
        dicc={'J': [] , 'N': [], 'B': []}
        diseñoInicial=[[sg.Text('  ¿Desea comenzar?', background_color='#e96b27',font=("scruff", 35))],
                [sg.Button('Si', button_color=('black','#e96b27'),font=("scruff", 20)),
                sg.Button('No', button_color=('black','#e96b27'),font=("scruff", 20))]]

        #Muestro la ventana
        ventanaInicial = sg.Window('Sopa de letras',auto_size_buttons=False,background_color='#e96b27').Layout(diseñoInicial)

        #Espero información
        event, values = ventanaInicial.Read()
        resultado = None
        if event == 'Si':
            ventanaInicial.Close()
            dicc = ip.generarPalabras(dicc)
            if dicc == None or esVacio(dicc):
                sg.PopupError('Se decidio no jugar')
                return None,None
            else:
                resultado = sel.seleccion(dicc)
                if resultado == None:
                        return None
        return (dicc,resultado)

def jugar(palabras, config):
    jugar_modulo.jugar(palabras, config)
