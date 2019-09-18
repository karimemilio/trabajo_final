"""Validaciones se encarga de validar cada una de las palabras ingresadas , primero con wikitionary y despues con Pattern, y partir de sus resultados
    hacer diferentes comparaciones para generar el reporte deseado"""
import PySimpleGUI as sg
from pattern.web import Wiktionary,SEARCH
from pattern.web import SEARCH
from pattern.text.es import tag

def hashTipo (tipo):
    if tipo == 'NN':
        return 'sustantivo'
    elif tipo == 'JJ':
        return  'adjetivo'
    else:
        return 'verbo'

def validarPattern(pal): #Devuelve adjetivo, sustantivo, verbo
    tipo = (tag(pal))[0][1]
    if tipo:
        tipo = hashTipo(tipo)
        return (True,tipo)
    else:
        return (False)

def validarWiki(pal): #Devuelve adjective,noun,verb
    wik = Wiktionary(language = 'es')
    try:
        tipo = wik.search(pal, type = SEARCH).sections[3].title.split()[0].lower()
        secc = wik.search(pal, type = SEARCH).sections[3].string
        secc = secc.split('\n')
        for i in range(0,len(secc)):
            if (secc[i] != ''):
                if (secc[i][0] == '1'):
                    defi = secc[i][1:]
                    break
        return(True,tipo,defi)
    except:
        return(False,False,False)

def validar(dat,lis,archivo):
    arch = open(archivo, "ta")
    vw = validarWiki(dat) #Retorna tupla (bool,tipo,definicion)
    vp = validarPattern(dat) #Devuelve tupla (boolean,tipo)
    if vw[0]:
        if (dat in lis):
            return (False,vw[1], 'DEL')
        if vp[0]:
            if vw[1] != vp[1]:
                arch.write(dat + ": La clasificación de Wiktionary no coincide con la de Pattern. Tomamos como válida la clasificación de Wiktionary\n")
        else:
            arch.write(dat + ": La clasificación de Pattern es inváida. Tomamos como válida la clasificación de Wiktionary\n")
        arch.close()
        return vw
    else:
        if (dat in lis):
            arch.close()
            return (False,vp[1], 'DEL')
        if vp[0]:
            text = None
            arch.write(dat + ": La clasificación de Wiktionary es inváida. Tomamos como válida la clasificación de Pattern\n")
            defi = 'Ingrese una definicion para la palabra: ' + str(dat)
            text = sg.PopupGetText(defi, 'Definicion',background_color='#b3d4fc')
            if (text == None):
                arch.write(dat + ": No se encontró la palabra. No se ingresa\n")
                arch.close()
                return (False,1,None)
            arch.close()
            return (vp[0],vp[1],text)
        else:
            arch.write(dat + ": No se encontró la palabra. No se ingresa\n")
            arch.close()
            return (False,1,None)    #No se encontro ni en wikidictionary ni en pattern