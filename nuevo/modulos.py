import ingresar as ip
import seleccion as sel
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
        """Evalúa el contenido del diccionario de palabras.
        Devuelve True en caso de contener al menos una palabra en alguna de sus categorías y False en caso contrario"""
        if len(dicc['J']) > 0 and len(dicc['N']) > 0 and len(dicc['B']) > 0 :
                return False
        else:
                return True

def cargarInfo():
        """Muestra la ventana inicial. Pregunta al usuario si desea jugar o no.
        En caso afirmativo invoca a la ventana de ingreso de palabras,
        caso contrario devuelve valores nulos para finalizar la ejecución.
        Crea un diccionario con las claves de las palabras a usar:
        J para adjetivos, N para sustantivos y B para verbos."""
        dicc={'J': [] , 'N': [], 'B': []}       #Crea el diccionario de palabras

        diseñoInicial=[[sg.Text('  ¿Desea comenzar?', background_color='#e96b27',font=("scruff", 35))], #Diseño de la ventana inicial
                [sg.Button('Si', button_color=('black','#e96b27'),font=("scruff", 20)),
                sg.Button('No', button_color=('black','#e96b27'),font=("scruff", 20))]]

        #Muestra la ventana inicial que consulta si desea comenzar
        ventanaInicial = sg.Window('Sopa de letras',auto_size_buttons=False,background_color='#e96b27').Layout(diseñoInicial)

        #Espera información
        event,values = ventanaInicial.Read()
        ventanaInicial.Close()
        if event == 'Si':
            dicc = ip.generarPalabras(dicc)             #Carga el diccionario con palabras
            if dicc == None or esVacio(dicc):           #Comprueba que se hayan ingresado palabras
                return None,None                        #Si no cargó palabras, se retorna None
            else:
                resultado = sel.seleccion(dicc)         #Si cargó palabras, se llama al módulo de configuración de juego y selección de palabras
                return (dicc,resultado)                 #Devuelve el diccionario de palabras y el diccionario de configuración
        else:
                return None,None                        #Si no quiso jugar, retorna None
