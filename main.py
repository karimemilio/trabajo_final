import PySimpleGUI as sg
from secciones.ingresar_palabras import *

class aplicacion():
    # def __init__(self):
    #     """Inicializar valores"""
    #     self.dicc={'JJ': [] , 'NN': [], 'VB': []}    #Creo un diccionario vacío

    def cargarInfo:
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
            return
        #armar 

    def main():
        """Ejecución de la aplicación"""
        dicc = cargarInfo()
        armarSopa(dicc)
    
if __name__=='__main__':	#Esta condicion se cumple si el módulo no es importado
    aplicacion().main()