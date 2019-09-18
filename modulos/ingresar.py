"""Este modulo se encarga a medida que se va ingresando palabras procesar la informacion ingresando o no la palabra a la lista de la grilla,tambien
    va editando el mensaje que aparece cada vez q se va ingresando una palabra"""

import PySimpleGUI as sg
import validaciones
import modulos

def borrar(palabra, dicc, tipos, lista_palabras, msje):
    mensaje= msje.join('La palabra se eliminará de la lista')
    if confirmar(mensaje):
        tipo = tipos[palabra]
        dicc[tipo] = list(filter(lambda di:di['palabra']!=palabra, dicc[tipo]))
        lista_palabras.remove(palabra)
        return 'La palabra se eliminó'

def crearArchivo(arch):
    archivo = open(arch, "tw")
    archivo.write('Reporte:\n\n')
    archivo.close()

def verReporte():
        reporte = "reporte.txt"
        with open(reporte, "r") as f:
            lineas = f.readlines()
        texto = ''
        for linea in lineas:
            texto += linea
        sg.Popup(texto,background_color='#b3d4fc', title= 'Reporte')

def agregarPredefinidas(dicc):
    if dicc['adjetivo'] == []:
        dicc['adjetivo'].append({ 'palabra': 'bonito', 'descripcion': 'Que tiene belleza o atractivo y resulta agradable de contemplar o de escuchar.'})
    if dicc['sustantivo'] == []:
        dicc['sustantivo'].append({ 'palabra': 'mesa', 'descripcion': 'Mueble formado por un tablero horizontal, sostenido por uno o varios pies, con la altura conveniente para poder realizar alguna actividad sobre ella o dejar cosas encima.'})
    if dicc['verbo'] == []:
        dicc['verbo'].append({ 'palabra': 'correr', 'descripcion': 'Desplazarse [una persona o un animal] rápidamente con pasos largos y de manera que levanta un pie del suelo antes de haber apoyado el otro.'})
    return dicc

def confirmar(msje):
    layout = [[sg.Text(msje,background_color='#b3d4fc')],[sg.Text('Está seguro que desea continuar?',background_color='#b3d4fc')],[sg.Button('Si',button_color=('black','#AEA79F')),sg.Button('Cancelar',button_color=('black','#AEA79F'))]]
    confirm = sg.Window('Atención!',background_color='#b3d4fc').Layout(layout)
    press, data = confirm.Read()
    if press == 'Si':
        confirm.Close()
        return True
    else:
        confirm.Close()
        False

def mostrarPalabras(dicc):
    lis = []
    for pos in dicc:
        for pal in dicc[pos]:
            lis.append(pal['palabra'])
    return lis

def generarPalabras(dicc):
    #Creo el diseño de la ventana de ingreso de palabras
    mensaje = 'Lista de palabras:'
    diseñoPalabras = [[sg.Text('Ingrese una palabra',background_color='#b3d4fc',font=("scruff", 25))],
          [sg.Input(do_not_clear=False,background_color='#84c3be'),sg.Button('OK', button_color=('Black', '#AEA79F')), sg.Button('?', button_color=("White", "Red"))],
          [sg.Text(' ', key= 'mensaje',size=(55,1),background_color='#b3d4fc')],
          [sg.Listbox(values=mostrarPalabras(dicc), key='lp', select_mode=None, change_submits=False, enable_events=False, size=(30, 6),background_color='#84c3be'),sg.Button('Borrar',  button_color=('Black', '#AEA79F'))],
          [sg.Button('Avanzar', button_color=('Black', '#AEA79F')),sg.Button('Salir', button_color=('Black', '#AEA79F')),sg.Button('Ver reporte', button_color=('Black', '#AEA79F'))]]

    #Muestro la ventana de ingreso de palabras (carga)
    ventanaPalabras = sg.Window('Sopa de letras',auto_size_text=True,default_element_size=(40, 1),background_color='#b3d4fc').Layout(diseñoPalabras)
    
    #Proceso la información
    lista_palabras = []
    dicc_tipos = {}
    arch = "reporte.txt"
    crearArchivo(arch)
    while True:     #Se ingresan palabras hasta que se haga clic en 'Finalizar'
        boton, datos = ventanaPalabras.Read()   #Leo los datos de la ventana
        if boton is None:
            ventanaPalabras.Close()
            return None
        elif boton == 'Salir':
            msje = 'Usted está a punto de salir del juego...'
            if confirmar(msje):
                ventanaPalabras.Close()
                return None
        elif boton == 'Avanzar':
            if modulos.esVacio(dicc):
                msje = 'No se ingresaron palabras suficientes.\nDeberá ingresar al menos una por cada tipo de palabra\nSi continúa se completará el diccionario de palabras con predefinidas'
                if confirmar(msje):
                    dicc = agregarPredefinidas(dicc)
                    ventanaPalabras.Close()
                    return (dicc)
            else:
                msje = 'Las palabras fueron almacenadas correctamente'
                if confirmar(msje):
                    ventanaPalabras.Close()
                    return (dicc)
        elif boton == '?':
            sg.Popup('Armado del diccionario de palabras:\n\n>Agregar palabra: Escribir un vocablo en el campo inferior y presionar "OK"\n>Eliminar palabra: Seleccionar una palabra de la lista y presionar "Borrar". También es posible escribir un vocablo existente en el campo inferior y presionar "OK"\n>Finalizar carga: Presionar "Avanzar"\n>Reporte de palabras: Muestra los conflictos que hubieron durante la carga de palabras. Presionar "Ver reporte"\n>Abandonar juego: Presionar "Salir"', title='Instrucciones',background_color='#b3d4fc',button_color=('black','#AEA79F'))
        elif boton == 'Ver reporte':
            try:
                verReporte()
            except:
                sg.Popup('Reporte inexistente')
        elif boton == 'Borrar':
            if len(datos['lp']) > 0:
                mensaje = borrar(datos['lp'][0],dicc, dicc_tipos,lista_palabras,'')
        else:
            if (len(lista_palabras) > 9):
                sg.Popup('Se alcanzó el límite de palabras a ingresar', background_color='#b3d4fc', button_color=('Black', '#AEA79F'))
            else:
                palabra = datos[0].lower()
                if palabra == '':
                    sg.Popup('No se ingresó ninguna palabra', title = 'Atención!', background_color='#b3d4fc')
                    mensaje='Ingrese una palabra en el espacio de arriba'
                elif len(palabra) < 3 or len(palabra) > 12:
                    mensaje='Ingrese una palabra de al menos 3 y a lo sumo 12 caracteres'
                else:
                    bool, tipo, defi = validaciones.validar(palabra,lista_palabras,arch) #Retorna tupla (bool,tipo,definicion)
                    if bool:
                        try:
                            dicc[tipo].append({ 'palabra': palabra, 'descripcion': ''.join(str(defi)) })
                            mensaje = 'La palabra fue ingresada correctamente'
                            lista_palabras.append(palabra)
                            dicc_tipos[palabra] = tipo
                        except:
                            sg.Popup('No se pudo agregar la palabra')
                    elif (defi == 'DEL'):
                        mensaje = borrar(palabra,dicc, dicc_tipos,lista_palabras,'La palabra ya fue ingresada.')
                    else:
                        sg.PopupError('La palabra ingresada no es valida')
        ventanaPalabras.FindElement('mensaje').Update(mensaje)
        ventanaPalabras.FindElement('lp').Update(values = mostrarPalabras(dicc))
