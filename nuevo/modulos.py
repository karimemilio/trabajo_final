import ingresar as ip
import seleccion as sel
import jugar as jugar_modulo
import PySimpleGUI as sg

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
<<<<<<< HEAD
            ventanaInicial.Close()
            dicc = ip.generarPalabras(dicc)
            if esVacio(dicc):
                sg.PopupError('Se decidio no jugar')
                return None,None
            else:
                resultado = sel.seleccion(dicc)
        return (dicc,resultado)
=======
            dicc, horizontal = ip.generarPalabras(dicc)
        # else:
        #     print('No quiso jugar :(')
        ventanaInicial.Close()
        if esVacio(dicc):
            return None,None
        else:
            resultado = sel.seleccion(dicc)
            resultado['horizontal'] = horizontal
        return (dicc, resultado)
>>>>>>> 0422f448a8c2db6ca43b7bb270ceaf388fa12cf0

def jugar(palabras, config):
    jugar_modulo.jugar(palabras, config)
