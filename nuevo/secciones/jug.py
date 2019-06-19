import PySimpleGUI as sg
def orientacion():

        #Creo el diseño de la ventana
        diseñoInicial=[[sg.Text('  Elija orientacion', background_color='#e96b27',font=("scruff", 35))],
                [sg.Button('Horizontal', button_color=('black','#e96b27'),font=("scruff", 20)),
                sg.Button('Vertical', button_color=('black','#e96b27'),font=("scruff", 20))]]
        
        #Muestro la ventana
        ventanaInicial = sg.Window('orientacion',auto_size_buttons=False,background_color='#e96b27').Layout(diseñoInicial) 
        
        #Espero información
        event, values = ventanaInicial.Read()
        return event
        ventanaInicial.Close()

def calcular_long(dic):        #Retorna la palabra mas larga
	key = dic.keys()
	maxi = 0
	for i in key:
		if (len(i) >  maxi):
			maxi = len(i)
	return maxi
